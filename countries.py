"""Country name -> landmark thumbnail.
Uses assets/countries/<code>.jpg|png|webp if you add a photo, otherwise the bundled SVG illustration."""
import base64
import re
from functools import lru_cache
from pathlib import Path

ASSETS = Path(__file__).with_name("assets") / "countries"
NAMES = {
    "fr": ["france"], "gb": ["united kingdom", "uk", "u.k.", "great britain", "britain", "england", "scotland", "wales"],
    "us": ["united states", "usa", "u.s.", "u.s.a.", "us", "america", "united states of america"], "ca": ["canada"],
    "au": ["australia"], "de": ["germany", "deutschland"], "it": ["italy"], "es": ["spain"],
    "nl": ["netherlands", "the netherlands", "holland"], "ch": ["switzerland"], "dk": ["denmark"], "se": ["sweden"],
    "no": ["norway"], "fi": ["finland"], "at": ["austria"], "be": ["belgium"], "ie": ["ireland"], "jp": ["japan"],
    "cn": ["china"], "kr": ["south korea", "korea", "republic of korea"], "tw": ["taiwan"], "sg": ["singapore"],
    "my": ["malaysia"], "tr": ["turkey", "turkiye", "t\u00fcrkiye"], "hu": ["hungary"], "pl": ["poland"],
    "cz": ["czech republic", "czechia"], "nz": ["new zealand"], "ae": ["united arab emirates", "uae", "dubai", "abu dhabi"],
    "sa": ["saudi arabia"], "qa": ["qatar"], "ru": ["russia", "russian federation"], "in": ["india"], "eg": ["egypt"],
    "br": ["brazil"], "mx": ["mexico"], "gr": ["greece"], "pt": ["portugal"], "za": ["south africa"],
}
LOOKUP = {n: code for code, names in NAMES.items() for n in names}
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp", ".svg": "image/svg+xml"}


def code_for(country):
    """'Germany' -> 'de'; 'Austria, Netherlands' -> 'at'; unknown / 'Any country' -> 'globe'."""
    for part in re.split(r"[,/&;]|\band\b", (country or "").lower()):
        part = re.sub(r"\(.*?\)", "", part).strip(" .")
        if part in LOOKUP:
            return LOOKUP[part]
    return "globe"


@lru_cache(maxsize=None)
def data_uri(code):
    for ext in (".jpg", ".jpeg", ".png", ".webp", ".svg"):
        p = ASSETS / f"{code}{ext}"
        if p.exists():
            return f"data:{MIME[ext]};base64," + base64.b64encode(p.read_bytes()).decode()
    return data_uri("globe") if code != "globe" else ""


def css_for(codes):
    """CSS classes .c-<code>{background-image:...} for the countries shown on screen."""
    return "".join(f".c-{c}{{background-image:url({data_uri(c)});}}\n" for c in sorted(set(codes)) if data_uri(c))
