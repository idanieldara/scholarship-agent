"""Scholarship agent: Gemini + Google Search grounding -> structured JSON.
Retries on 503, skips quickly on 429 (quota), falls back to a second model."""
import json
import os
import time
from datetime import date
from typing import Optional

from google import genai
from google.genai import types
from pydantic import BaseModel

MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
FALLBACK_MODEL = os.getenv("GEMINI_FALLBACK_MODEL", "gemini-2.5-flash-lite")
RETRY_CODES = {500, 502, 503, 504}

REGIONS = ["Europe (EU/EEA and Switzerland)", "United Kingdom and Ireland", "North America",
           "East and South-East Asia", "Middle East, Turkey and Central Asia",
           "Australia, New Zealand and Oceania", "Africa and Latin America"]


class Scholarship(BaseModel):
    title: str
    level: list[str]                    # Bachelor / Master / PhD / Postdoc / Other
    country: str
    university: Optional[str]
    fields: list[str]
    funding_type: str                   # Full / Partial / Tuition only / Unknown
    amount: Optional[str]
    deadline: Optional[str]             # YYYY-MM-DD or null
    eligible_nationalities: list[str]   # ["Any"] if open to all
    language_requirement: Optional[str]
    url: str
    summary: str


class Enrichment(BaseModel):
    url: str
    funding_type: str
    amount: Optional[str]
    fields: list[str]
    eligible_nationalities: list[str]
    language_requirement: Optional[str]
    summary: str


def _models(model):
    first = model or MODEL
    return [first] + ([FALLBACK_MODEL] if FALLBACK_MODEL and FALLBACK_MODEL != first else [])


def _gen(client, models, contents, cfg, log=None):
    """generate_content with retries (503 etc.) and model fallback."""
    last = None
    for m in models:
        for attempt in range(4):
            try:
                return client.models.generate_content(
                    model=m, contents=contents, config=types.GenerateContentConfig(**cfg))
            except Exception as e:
                last = e
                code = getattr(e, "code", None)
                msg = str(e)
                if code == 429 or "RESOURCE_EXHAUSTED" in msg:
                    if log:
                        log(f"🚫 {m}: quota / rate limit (429): {msg[:300]}")
                    break              # retrying will not help -> next model
                if not (code in RETRY_CODES or "UNAVAILABLE" in msg or "overloaded" in msg.lower()):
                    raise
                wait = 3 * 2 ** attempt            # 3, 6, 12, 24 s
                if log:
                    log(f"⏳ {m}: temporary error ({code}). Retrying in {wait}s…")
                time.sleep(wait)
        if log:
            log(f"↪️ Switching to fallback model after errors on {m}")
    raise last


def _to_json(client, models, instructions, text, schema, log):
    r = _gen(client, models, f"{instructions}\n\nTEXT:\n{text}",
             dict(response_mime_type="application/json", response_schema=schema), log)
    try:
        return json.loads(r.text or "[]")
    except json.JSONDecodeError:
        return []


def _search_once(client, models, levels, where, field, nationality, funding, limit, out_lang, log, known=None):
    if not nationality or nationality.startswith("Any"):
        nat = "open to international students of any nationality"
    else:
        nat = f"that citizens of {nationality} are eligible to apply for"
    skip = ("\nThe user already has the scholarships below saved. Do NOT list them again; find DIFFERENT ones:\n- "
            + "\n- ".join(known[:120])) if known else ""
    prompt = f"""Today is {date.today().isoformat()}.
Use Google Search (run several different searches) to find as many REAL scholarships as you can,
up to {limit}, {nat}.
Filters:
- Education level: {", ".join(levels) or "any"}
- Study destination: {where}
- Field of study: {field or "any field"}
- Funding: {funding or "any"}
Include scholarships that are open now OR are annual programmes that reopen within the next 12 months.
Skip ones that no longer exist. Prefer official pages. Do NOT stop after a few results.
For each scholarship give: title, level, country, university, fields, funding type, amount,
deadline, eligible nationalities, language requirement, official URL, and a 1-2 sentence summary.
Write the summary in {out_lang}; keep titles, names and URLs in their original form.
Do not invent anything; write 'unknown' if unsure.{skip}"""
    r1 = _gen(client, models, prompt, dict(tools=[types.Tool(google_search=types.GoogleSearch())]), log)
    raw = r1.text or ""
    if not raw.strip():
        return []
    data = _to_json(
        client, models,
        "Convert the scholarship information below into a JSON array. level values from "
        "[Bachelor, Master, PhD, Postdoc, Other]; funding_type from [Full, Partial, Tuition only, Unknown]; "
        "deadline YYYY-MM-DD or null; eligible_nationalities=[\"Any\"] if open to all; null for unknown "
        "optional values. Keep summaries in their current language. "
        "Do not add scholarships that are not in the text.",
        raw, list[Scholarship], log)
    items = []
    for d in data:
        try:
            it = Scholarship(**d).model_dump()
            it["source"] = "ai-search"
            items.append(it)
        except Exception:
            continue
    return items


def search_scholarships(api_key, levels, countries, field, nationality, funding,
                        per_pass=15, deep=True, model=None, out_lang="English", log=None, known_titles=None):
    """No countries given -> all countries (one pass per world region when deep=True)."""
    client = genai.Client(api_key=api_key)
    models = _models(model)
    if countries:
        passes = [", ".join(countries[i:i + 3]) for i in range(0, len(countries), 3)]
    elif deep:
        passes = REGIONS
    else:
        passes = ["any country in the world"]
    found = {}
    for n, where in enumerate(passes, 1):
        if log:
            log(f"🔎 Pass {n}/{len(passes)}: {where}")
        try:
            for it in _search_once(client, models, levels, where, field, nationality,
                                   funding, per_pass, out_lang, log, known_titles):
                found[(it["title"].lower(), it["country"].lower())] = it
        except Exception as e:
            if log:
                log(f"⚠️ Pass {n} failed: {e}")
        if log:
            log(f"   total so far: {len(found)}")
        if n < len(passes):
            time.sleep(5)          # be gentle with per-minute rate limits
    return list(found.values())


def enrich(api_key, items, model=None, batch=5, out_lang="English", log=None):
    """Read each scholarship page (URL context) and fill funding, nationalities, fields."""
    client = genai.Client(api_key=api_key)
    models = _models(model)
    by_url = {it["url"]: it for it in items}
    urls = list(by_url)
    for i in range(0, len(urls), batch):
        chunk = urls[i:i + batch]
        if log:
            log(f"✨ Reading pages {i + 1}-{i + len(chunk)} of {len(urls)}")
        try:
            r1 = _gen(client, models,
                      "Read each of these scholarship pages and report, for EACH url: funding type "
                      "(Full/Partial/Tuition only), amount, eligible nationalities (say 'Any' if open to "
                      "all international students, or list countries/regions), fields of study, "
                      "language requirement, and a 1-2 sentence summary written in "
                      f"{out_lang}.\n" + "\n".join(chunk),
                      dict(tools=[types.Tool(url_context=types.UrlContext())]), log)
            data = _to_json(
                client, models,
                "Return a JSON array with one object per page. Keep each url exactly as written. "
                "funding_type from [Full, Partial, Tuition only, Unknown]. Keep the summary language.",
                r1.text or "", list[Enrichment], log)
            for d in data:
                try:
                    e = Enrichment(**d).model_dump()
                except Exception:
                    continue
                if e["url"] in by_url:
                    tgt = by_url[e["url"]]
                    for k in ("funding_type", "amount", "fields", "eligible_nationalities",
                              "language_requirement", "summary"):
                        if e[k]:
                            tgt[k] = e[k]
        except Exception as ex:
            if log:
                log(f"⚠️ Batch failed: {ex}")
        if i + batch < len(urls):
            time.sleep(3)
    return list(by_url.values())
