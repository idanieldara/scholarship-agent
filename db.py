"""Tiny SQLite store + local filtering."""
import json
import sqlite3
from datetime import date, datetime

DB = "scholarships.db"
OPEN_WORDS = {"any", "all", "international", "worldwide", "all nationalities"}


def _conn():
    c = sqlite3.connect(DB)
    c.execute("CREATE TABLE IF NOT EXISTS s (k TEXT PRIMARY KEY, data TEXT, updated TEXT)")
    return c


def country_parts(c):
    parts = [p.strip(" .-") for p in (c or "").split(",")]
    return [p for p in parts if len(p) > 1] or ["Unknown"]


def key_of(it):
    return it["title"].strip().lower() + "|" + it["country"].strip().lower()


def save(items):
    with _conn() as c:
        for it in items:
            it["country"] = ", ".join(country_parts(it.get("country")))
            c.execute("INSERT OR REPLACE INTO s VALUES (?,?,?)",
                      (key_of(it), json.dumps(it, ensure_ascii=False), datetime.now().isoformat()))


def all_items():
    with _conn() as c:
        return [json.loads(r[0]) for r in c.execute("SELECT data FROM s")]


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
