"""Crawlers for scholarship listing websites (no AI, no API cost)."""
import re
import time
from datetime import date
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
_session = requests.Session()
_session.headers.update(HEADERS)
MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
DAY_RE = re.compile(r"(\d{1,2})\s+([A-Za-z]{3,9})\.?,?\s+(\d{4})")        # 15 Dec 2026
US_RE = re.compile(r"([A-Za-z]{3,9})\.?\s+(\d{1,2}),?\s+(\d{4})")         # December 15, 2026
MONTH_YEAR_RE = re.compile(r"\b([A-Za-z]{3,9})\.?\s+(\d{4})\b")          # Dec 2026
LEVEL_RE = re.compile(r"(bachelor|undergrad|master|mba|postgrad|ph\.?d|doctor|post-?doc|fellowship|diploma)", re.I)

# ---------------------------------------------------------------- registry
SITES = {"Scholars4Dev": {"url": "https://www.scholars4dev.com/", "kind": "s4d"}}
for _label, _slug, _lvl, _fund in [
        ("Masters", "masters", "Master", None), ("PhD", "phd", "PhD", None),
        ("MBA", "mba", "Master", None), ("Undergraduate", "undergraduate", "Bachelor", None),
        ("Postgraduate", "postgraduate", "Master", None), ("Fellowship", "fellowship", None, None),
        ("Fully funded", "fully-funded", None, "Full")]:
    SITES[f"ScholarshipTab – {_label}"] = {
        "url": f"https://www.scholarshiptab.com/{_slug}", "kind": "family", "level": _lvl, "funding": _fund}
for _label, _slug, _lvl in [("Masters", "masters", "Master"), ("PhD", "phd", "PhD"),
                            ("Undergraduate", "undergraduate", "Bachelor")]:
    SITES[f"ScholarshipSet (Africa) – {_label}"] = {
        "url": f"https://www.scholarshipset.com/{_slug}", "kind": "family", "level": _lvl}
for _name, _url, _country in [
        ("GermanyScholarships.de", "https://www.germanyscholarships.de/", "Germany"),
        ("UKScholarships.uk", "https://www.ukscholarships.uk/", "United Kingdom"),
        ("ScholarshipCA.com (Canada)", "https://www.scholarshipca.com/", "Canada"),
        ("UScholarships.us (USA)", "https://www.uscholarships.us/", "United States"),
        ("ScholarshipAU.com (Australia)", "https://www.scholarshipau.com/", "Australia")]:
    SITES[_name] = {"url": _url, "kind": "family", "country": _country}


def guess_kind(url):
    return "s4d" if "scholars4dev.com" in url else "family"


# ---------------------------------------------------------------- helpers
def parse_dates(text):
    out = []

    def add(d, m, y):
        mo = MONTHS.get(m[:3].lower())
        if mo:
            try:
                out.append(date(int(y), mo, int(d)))
            except ValueError:
                pass

    for m, d, y in US_RE.findall(text):
        add(d, m, y)
    rest = US_RE.sub(" ", text)
    for d, m, y in DAY_RE.findall(rest):
        add(d, m, y)
    rest = DAY_RE.sub(" ", rest)
    for m, y in MONTH_YEAR_RE.findall(rest):
        add(28, m, y)          # month only -> end of month (approx.)
    return out


def pick_deadline(dates):
    if not dates:
        return None
    upcoming = sorted(d for d in dates if d >= date.today())
    return (upcoming[0] if upcoming else max(dates)).isoformat()


def normalize_levels(text):
    t = (text or "").lower()
    levels = []
    if "bachelor" in t or "undergrad" in t:
        levels.append("Bachelor")
    if "master" in t or "mba" in t or "postgrad" in t:
        levels.append("Master")
    if re.search(r"ph\.?d|doctor", t) and "postdoc" not in t:
        levels.append("PhD")
    if re.search(r"post-?doc", t):
        levels.append("Postdoc")
    return levels or ["Other"]


def _clean_country(c):
    c = re.sub(r"\s+,", ",", c or "").strip(" .,-")
    if len(c) < 2:
        return "Unknown"
    return "Any country" if c.lower().startswith("any") else c


def _item(title, level, country, org, deadline_text, url, summary, amount=None):
    return {
        "title": title, "level": level, "country": _clean_country(country), "university": org,
        "fields": [], "funding_type": "Unknown", "amount": amount,
        "deadline": pick_deadline(parse_dates(deadline_text or "")),
        "deadline_text": deadline_text or None,
        "eligible_nationalities": ["Unknown"], "language_requirement": None,
        "url": url, "summary": summary or "", "source": "",
    }


# ---------------------------------------------------------------- Scholars4Dev
def _value_after(lines, key):
    for i, line in enumerate(lines):
        if line.lower().startswith(key.lower()):
            val = line.split(":", 1)[1].strip() if ":" in line else ""
            if not val and i + 1 < len(lines):
                val = lines[i + 1].strip()
            return val
    return ""


def _container(h2):
    node = h2
    for _ in range(4):          # climb to the per-post container
        if node.parent is not None and len(node.parent.find_all("h2")) == 1:
            node = node.parent
        else:
            break
    return node


def parse_s4d(soup, base_url="", level_hint=None, default_country=None):
    items = []
    for h2 in soup.find_all("h2"):
        a = h2.find("a", href=True)
        if not a or not re.search(r"scholars4dev\.com/\d+/", a["href"]):
            continue
        lines = [l.strip() for l in _container(h2).get_text("\n", strip=True).split("\n") if l.strip()]
        title = a.get_text(strip=True)
        deadline_text = _value_after(lines, "Deadline")
        study_in = _value_after(lines, "Study in")
        idx = next((i for i, l in enumerate(lines)
                    if l != title and len(l) < 80 and LEVEL_RE.search(l)
                    and not l.lower().startswith(("deadline", "study in"))), None)
        level_line = lines[idx] if idx is not None else ""
        org = lines[idx - 1] if idx and lines[idx - 1] != title else None
        if not (deadline_text or study_in or level_line):
            continue        # a "Top 20 ..." list post, not a single scholarship
        start = next((l for l in lines if l.lower().startswith(("course starts", "next term"))), "")
        summary = " | ".join(x for x in [level_line, start] if x) or "Listed on Scholars4Dev."
        items.append(_item(title, normalize_levels(level_line), study_in, org, deadline_text,
                           a["href"], summary))
    return items


# ---------------------------------------------------------------- ScholarshipTab family
LABEL_RE = r"(?:Published|Posted|Type|Study in|Value|Deadline)"


def _field(text, label):
    m = re.search(rf"\b{label}:\s*(.*?)(?=\s+{LABEL_RE}:|$)", text)
    return re.sub(r"\s+,", ",", m.group(1)).strip() if m else ""


def parse_family(soup, base_url="", level_hint=None, default_country=None):
    items = []
    for h2 in soup.find_all("h2"):
        a = h2.find("a", href=True)
        if not a or "scholarship" not in a["href"].lower():
            continue
        text = _container(h2).get_text(" ", strip=True)
        if "Deadline:" not in text:
            continue
        title = a.get_text(strip=True)
        type_txt = _field(text, "Type")
        deadline_text = _field(text, "Deadline")
        if deadline_text.lower().startswith("not specified"):
            deadline_text = ""
        i = text.find(title)
        rest = text[i + len(title):] if i >= 0 else text
        m = re.search(rf"\b{LABEL_RE}:", rest)
        desc = (rest[:m.start()] if m else rest[:300]).strip()[:400]
        items.append(_item(
            title, normalize_levels(type_txt or level_hint or title),
            _field(text, "Study in") or default_country, None, deadline_text,
            urljoin(base_url, a["href"]), desc, _field(text, "Value") or None))
    return items


# ---------------------------------------------------------------- crawling
def _get(url):
    root = "{0.scheme}://{0.netloc}/".format(urlparse(url))
    r = _session.get(url, headers={"Referer": root}, timeout=30)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def _page_template(soup, base_url):
    """Find the pagination link 'page 2' and turn it into a URL template."""
    for a in soup.find_all("a", href=True):
        if a.get_text(strip=True) == "2":
            href = urljoin(base_url, a["href"]).split("?")[0]
            m = re.match(r"^(.*?)(\d+)(/?)$", href)
            if m:
                return m.group(1) + "{n}" + m.group(3)
    return None


def crawl(url, kind=None, max_pages=10, level_hint=None, country=None, funding=None,
          progress=None, delay=1.0):
    kind = kind or guess_kind(url)
    parse = parse_s4d if kind == "s4d" else parse_family
    source = urlparse(url).netloc.replace("www.", "")
    soup = _get(url)
    if soup is None:
        return []
    template = _page_template(soup, url)
    items, seen, n = [], set(), 1
    while True:
        new = [it for it in parse(soup, url, level_hint, country) if it["url"] not in seen]
        for it in new:
            seen.add(it["url"])
            it["source"] = source
            if funding:
                it["funding_type"] = funding
            items.append(it)
        if progress:
            progress(n, max_pages, len(items))
        if n >= max_pages or not template or (n > 1 and not new):
            break
        n += 1
        time.sleep(delay)
        soup = _get(template.replace("{n}", str(n)))
        if soup is None:
            break
    return items
