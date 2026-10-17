"""Local SQLite store with duplicate detection / merging, plus filtering helpers.

Scholarships coming from several websites and from the AI search are matched by URL and by a
normalised title; matches are merged into one record instead of being listed twice."""
import json
import re
import sqlite3
from datetime import date, datetime
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urlparse

DB = str(Path(__file__).with_name("scholarships.db"))
OPEN_WORDS = {"any", "all", "international", "worldwide", "all nationalities"}
NOISE = {"scholarship", "scholarships", "fellowship", "fellowships", "program", "programme", "programs",
         "programmes", "for", "the", "of", "in", "and", "to", "at", "a", "an", "with", "from", "on", "by",
         "fully", "funded", "international", "students", "student", "apply", "application", "applications",
         "open", "call", "now", "new"}
PLACEHOLDER_COUNTRIES = {"Any country", "Unknown"}


def _conn():
    c = sqlite3.connect(DB)
    c.execute("CREATE TABLE IF NOT EXISTS s (k TEXT PRIMARY KEY, data TEXT, updated TEXT)")
    return c


def country_parts(c):
    parts = [p.strip(" .-") for p in (c or "").split(",")]
    return [p for p in parts if len(p) > 1] or ["Unknown"]


def key_of(it):
    return it["title"].strip().lower() + "|" + it["country"].strip().lower()


# ------------------------------------------------------------------ duplicate detection
def _tokens(title):
    t = (title or "").lower().replace("&", " and ")
    t = re.sub(r"\b(19|20)\d{2}\b", " ", t)                         # drop years (2026, 2027 ...)
    words = re.findall(r"[^\W_]+", t, re.UNICODE)
    return [w for w in words if w not in NOISE and not w.isdigit()] or [w for w in words if not w.isdigit()] or words


def _url_key(url):
    try:
        p = urlparse((url or "").strip().lower())
    except ValueError:
        return ""
    path = p.path.rstrip("/")
    return p.netloc.replace("www.", "") + path if p.netloc and len(path) > 1 else ""


def _similar(a, ta, b, tb):
    if not a or not b or not (a & b):
        return False
    if a == b:
        return True
    small, big = (a, b) if len(a) <= len(b) else (b, a)
    if small <= big and len(small) >= 3 and len(big) - len(small) <= 3:   # "X Y Z" vs "X Y Z W"
        return True
    return len(a & b) / len(a | b) >= 0.75 and SequenceMatcher(None, ta, tb).ratio() >= 0.85


class _Index:
    def __init__(self):
        self.items, self.by_url, self.by_tokens, self.inv = [], {}, {}, {}

    def add(self, key, item):
        toks = _tokens(item.get("title"))
        idx = len(self.items)
        self.items.append((key, set(toks), " ".join(toks)))
        uk = _url_key(item.get("url"))
        if uk:
            self.by_url.setdefault(uk, key)
        self.by_tokens.setdefault(tuple(toks), key)
        for t in set(toks):
            self.inv.setdefault(t, []).append(idx)

    def find(self, item):
        uk = _url_key(item.get("url"))
        if uk in self.by_url:
            return self.by_url[uk]
        toks = _tokens(item.get("title"))
        if tuple(toks) in self.by_tokens:
            return self.by_tokens[tuple(toks)]
        s, text, cand = set(toks), " ".join(toks), set()
        for t in s:
            lst = self.inv.get(t, ())
            if len(lst) <= 200:                      # ignore very common words
                cand.update(lst)
        for idx in sorted(cand):
            key, s2, text2 = self.items[idx]
            if _similar(s, text, s2, text2):
                return key
        return None


# ------------------------------------------------------------------ merging
def _known(v):
    return v not in (None, "", "Unknown")


def _quality(it):
    return (_known(it.get("funding_type")) + bool(it.get("fields"))
            + any(n.lower() != "unknown" for n in (it.get("eligible_nationalities") or []))
            + bool(it.get("amount")) + bool(it.get("language_requirement")) + bool(it.get("university")))


def _union(a, b):
    return list(dict.fromkeys([*(a or []), *(b or [])]))


def _merge(old, new):
    """Combine two records of the same scholarship. Richer information always wins; a plain
    re-import never wipes data that AI enrichment filled in."""
    hi, lo = (old, new) if _quality(old) >= _quality(new) else (new, old)
    out = {**lo, **old}
    for k in ("university", "amount", "language_requirement", "summary"):
        out[k] = hi.get(k) or lo.get(k)
    out["funding_type"] = hi["funding_type"] if _known(hi.get("funding_type")) else (lo.get("funding_type") or "Unknown")
    if new.get("deadline") or new.get("deadline_text"):               # newest crawl knows the current deadline
        out["deadline"], out["deadline_text"] = new.get("deadline"), new.get("deadline_text")
    lv = _union(old.get("level"), new.get("level"))
    out["level"] = [x for x in lv if x != "Other"] or ["Other"]
    out["fields"] = _union(old.get("fields"), new.get("fields"))
    nat = _union(old.get("eligible_nationalities"), new.get("eligible_nationalities"))
    out["eligible_nationalities"] = [x for x in nat if x.lower() != "unknown"] or ["Unknown"]
    cp = _union(country_parts(old.get("country")), country_parts(new.get("country")))
    cp = [x for x in cp if x not in PLACEHOLDER_COUNTRIES] or cp
    out["country"] = ", ".join(cp)
    out["url"] = old.get("url") or new.get("url") or ""
    out["source"] = ", ".join(_union(str(old.get("source") or "").split(", "), str(new.get("source") or "").split(", "))).strip(", ")
    out["first_seen"] = old.get("first_seen", "")
    out["last_seen"] = max(old.get("last_seen") or "", new.get("last_seen") or "")
    return out


def _clean(raw, today):
    it = dict(raw)
    it["title"] = (it.get("title") or "").strip()
    it["country"] = ", ".join(country_parts(it.get("country")))
    it["level"] = list(it.get("level") or ["Other"])
    it["fields"] = list(it.get("fields") or [])
    it["eligible_nationalities"] = list(it.get("eligible_nationalities") or ["Unknown"])
    it["funding_type"] = it.get("funding_type") or "Unknown"
    it.setdefault("source", "ai-search")
    it.setdefault("first_seen", today)
    it["last_seen"] = today
    return it


def _core(it):
    return {k: v for k, v in it.items() if k != "last_seen"}


# ------------------------------------------------------------------ public API
def save(items):
    """Add new scholarships and merge duplicates / updates into existing records.
    Returns {"added", "updated", "unchanged", "duplicates_removed"}."""
    today = date.today().isoformat()
    with _conn() as c:
        rows = [(k, json.loads(d)) for k, d in c.execute("SELECT k, data FROM s ORDER BY rowid")]
    store, index, removed = {}, _Index(), 0
    for k, d in rows:                                    # existing rows; also merges old duplicates
        d.setdefault("first_seen", "")
        hit = index.find(d)
        if hit is None:
            store[k] = d
            index.add(k, d)
        else:
            store[hit] = _merge(store[hit], d)
            removed += 1
    added = updated = unchanged = 0
    for raw in items:
        it = _clean(raw, today)
        if not it["title"]:
            continue
        hit = index.find(it)
        if hit is None:
            k = key_of(it)
            while k in store:
                k += "+"
            store[k] = it
            index.add(k, it)
            added += 1
        else:
            merged = _merge(store[hit], it)
            if _core(merged) != _core(store[hit]):
                updated += 1
            else:
                unchanged += 1
            store[hit] = merged
    if added or updated or unchanged or removed:         # nothing to write for save([]) on a clean DB
        with _conn() as c:
            c.execute("DELETE FROM s")
            c.executemany("INSERT INTO s VALUES (?,?,?)",
                          [(k, json.dumps(v, ensure_ascii=False), datetime.now().isoformat()) for k, v in store.items()])
    return {"added": added, "updated": updated, "unchanged": unchanged, "duplicates_removed": removed}


def all_items():
    """Newest additions first (then the original order)."""
    with _conn() as c:
        items = [json.loads(r[0]) for r in c.execute("SELECT data FROM s ORDER BY rowid")]
    order = {id(it): n for n, it in enumerate(items)}        # later rows = added later
    items.sort(key=lambda i: (i.get("first_seen") or "", order[id(i)]), reverse=True)
    return items


def clear():
    with _conn() as c:
        c.execute("DELETE FROM s")


def nationality_ok(item, nat):
    """Unknown nationality rules count as a match (verify on the official page)."""
    if not nat or nat.startswith("Any"):
        return True
    for n in item.get("eligible_nationalities") or ["unknown"]:
        n = n.lower()
        if n in OPEN_WORDS or "unknown" in n or nat.lower() in n:
            return True
    return False


def is_open(item):
    d = item.get("deadline")
    if not d:
        return True
    try:
        return date.fromisoformat(d) >= date.today()
    except ValueError:
        return True


def needs_enrich(item):
    return item.get("funding_type") in (None, "", "Unknown") or \
        "Unknown" in (item.get("eligible_nationalities") or ["Unknown"])
