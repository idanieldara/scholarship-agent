import base64
import html
import json
import os
from datetime import date
from pathlib import Path

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
import agent      # noqa: E402  (after load_dotenv so env vars are read)
import countries  # noqa: E402
import db         # noqa: E402
import i18n       # noqa: E402
import sources    # noqa: E402

APP_NAME = "Dara Scholarship Agent"
SITE_URL = "https://danieldara.com"
SUPPORT_EMAIL = "daniel@danieldara.com"
SETTINGS_FILE = Path(__file__).with_name("settings.json")
PAGE_SIZE = 30

st.set_page_config(page_title=APP_NAME, page_icon="🎓", layout="wide")

LEVELS = ["Bachelor", "Master", "PhD", "Postdoc", "Other"]
FUNDING = ["Full", "Partial", "Tuition only", "Unknown"]
NATIONALITIES = ["Any (open to all)", "Iran", "Afghanistan", "Iraq", "Turkey", "Pakistan",
                 "India", "Bangladesh", "Egypt", "Nigeria", "Syria", "Lebanon", "Jordan",
                 "Saudi Arabia", "Kazakhstan", "Uzbekistan", "Azerbaijan", "Russia",
                 "Ukraine", "China", "Indonesia", "Brazil", "Mexico", "Other…"]
MODELS = [agent.MODEL] + [m for m in ["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-2.5-pro",
                                       "gemini-3-flash-preview", "gemini-3.1-pro-preview"]
                          if m != agent.MODEL]

CAP = ('<svg class="cap" viewBox="0 0 40 40" width="{s}" height="{s}"><polygon points="20,6 38,15 20,24 2,15" fill="#111827"/>'
       '<path d="M10 19v8c0 3.5 20 3.5 20 0v-8l-10 5z" fill="#1f2937"/><line x1="35" y1="16" x2="35" y2="27" stroke="#f5b82e" stroke-width="2"/>'
       '<circle cx="35" cy="28.5" r="2.2" fill="#f5b82e"/></svg>')


# ============================================================== helpers
@st.cache_resource
def _font_css():
    """Embed the Sans (IRANSansX) font as base64 so it loads without any server config."""
    css = ""
    for weight, name in ((400, "Regular"), (700, "Bold")):
        p = Path(__file__).with_name("static") / f"Sans-{name}.woff2"
        if p.exists():
            b64 = base64.b64encode(p.read_bytes()).decode()
            css += ("@font-face{font-family:'Sans';font-weight:%d;font-display:swap;"
                    "src:url(data:font/woff2;base64,%s) format('woff2');}\n" % (weight, b64))
    return css


def _initial_lang():
    """?lang=xx in the URL wins, then the last saved choice, then English."""
    q = st.query_params.get("lang")
    if q in i18n.LANGS:
        return q
    try:
        saved = json.loads(SETTINGS_FILE.read_text(encoding="utf-8")).get("lang")
        if saved in i18n.LANGS:
            return saved
    except Exception:
        pass
    return "en"


def _remember_lang(code):
    if st.query_params.get("lang") != code:
        st.query_params["lang"] = code
    try:
        if json.loads(SETTINGS_FILE.read_text(encoding="utf-8")).get("lang") == code:
            return
    except Exception:
        pass
    try:
        SETTINGS_FILE.write_text(json.dumps({"lang": code}), encoding="utf-8")
    except Exception:
        pass


if "lang" not in st.session_state:
    st.session_state["lang"] = _initial_lang()
lang = st.session_state["lang"]
RTL = lang in i18n.RTL
AI_LANG = i18n.AI_LANG[lang]


def T(key, **kw):
    return i18n.tr(lang, key, **kw)


def lvl(v):
    return i18n.label(lang, "lvl", v)


def fund(v):
    return i18n.label(lang, "fund", v)


def esc(x):
    return html.escape(str(x if x is not None else ""), quote=True)


# ============================================================== styling
BASE_CSS = """
.stApp{background:linear-gradient(180deg,#f2f5ff 0,#ffffff 460px);}
.block-container{max-width:1200px;padding-top:1.4rem;}
h2,h3{font-weight:800 !important;letter-spacing:-.01em;}
[data-testid="stSidebar"]{background:#fff;border-inline-end:1px solid #eef0f6;}
[data-testid="stSidebar"][aria-expanded="false"]{display:none !important;}
.logo{display:flex;align-items:center;gap:10px;font-weight:800;font-size:1.08rem;color:#0f172a;margin:2px 0 16px;direction:ltr;}
.accent{color:#ef4444;}
[data-testid="stSidebar"] [role="radiogroup"]{gap:6px;}
[data-testid="stSidebar"] [role="radiogroup"] label{padding:10px 14px;border-radius:12px;width:100%;cursor:pointer;color:#334155;font-weight:600;}
[data-testid="stSidebar"] [role="radiogroup"] label>div:first-child{display:none;}
[data-testid="stSidebar"] [role="radiogroup"] label:hover{background:#f3f4f8;}
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked){background:#fde8e8;color:#ef4444;}
[data-testid="stSidebar"] [data-testid="stExpander"]{border:0;background:transparent;}
[data-testid="stSidebar"] [data-testid="stExpander"] summary{padding:6px 14px;border-radius:12px;font-weight:600;color:#334155;}
[data-testid="stSidebar"] [data-testid="stExpander"] summary:hover{background:#f3f4f8;}
.quote{margin-top:22px;padding:18px 14px;border-radius:16px;background:linear-gradient(180deg,#fff,#f4f7ff);border:1px solid #eef0f6;text-align:center;color:#475569;font-size:.88rem;}
.quote i{display:block;font-size:1.05rem;color:#0f172a;margin:6px 0 4px;font-weight:600;}
.hero{text-align:center;padding:.4rem 0 .6rem;}
.hero .brand{display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap;}
.hero h1{font-size:2.7rem;font-weight:800;margin:0;padding:0;color:#0f172a;letter-spacing:-.02em;line-height:1.15;}
.hero .tag{color:#64748b;font-size:1.08rem;margin:.5rem 0 1.2rem;}
.feats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;text-align:start;}
.feat{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid #eef0f6;border-radius:16px;padding:12px 14px;box-shadow:0 4px 14px rgba(15,23,42,.04);}
.fi{flex:0 0 44px;height:44px;border-radius:50%;display:grid;place-items:center;font-size:20px;}
.fi.a{background:#fde8e8}.fi.b{background:#e3eeff}.fi.c{background:#ddf6ec}.fi.d{background:#ebe7ff}
.feat b{display:block;color:#0f172a;font-size:.95rem;}.feat span.d{color:#64748b;font-size:.8rem;}
.stats{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:14px 0 10px;}
.stat{background:#fff;border:1px solid #eef0f6;border-radius:16px;padding:10px 22px;min-width:160px;box-shadow:0 4px 14px rgba(15,23,42,.04);}
.stat b{display:block;font-size:1.55rem;color:#ef4444;line-height:1.3;}.stat b.sm{font-size:1.05rem;line-height:2;}.stat span{color:#64748b;font-size:.82rem;}
[data-baseweb="tab-list"]{background:#f1f3f9;border-radius:12px;padding:4px;gap:4px;width:fit-content;max-width:100%;border:0;}
[data-baseweb="tab-highlight"],[data-baseweb="tab-border"]{display:none !important;}
button[data-baseweb="tab"]{border-radius:9px;padding:8px 16px;height:auto;font-weight:600;}
button[data-baseweb="tab"][aria-selected="true"]{background:#ef4444;}
button[data-baseweb="tab"][aria-selected="true"] *{color:#fff !important;}
[data-testid="stVerticalBlockBorderWrapper"]{border-radius:18px;border-color:#eceff5;background:#fff;box-shadow:0 6px 24px rgba(15,23,42,.05);}
[data-baseweb="select"]>div,[data-baseweb="input"]>div,[data-baseweb="base-input"]{border-radius:10px;}
button[kind="primary"]{border-radius:10px;font-weight:700;}
details.sch{background:#fff;border:1px solid #eceff5;border-radius:16px;margin:0 0 12px;box-shadow:0 2px 10px rgba(15,23,42,.04);overflow:hidden;}
details.sch:hover{box-shadow:0 8px 22px rgba(15,23,42,.09);}
details.sch summary{list-style:none;display:flex;align-items:center;gap:16px;padding:12px;cursor:pointer;}
details.sch summary::-webkit-details-marker{display:none;}
.thumb{flex:0 0 112px;height:80px;border-radius:12px;background-size:cover;background-position:center;background-color:#e8eefc;}
.info{flex:1;min-width:0;}
.ttl{font-weight:700;color:#0f172a;font-size:1rem;line-height:1.4;}
.meta{display:flex;flex-wrap:wrap;gap:4px 16px;margin-top:6px;color:#64748b;font-size:.82rem;}
.ic{filter:grayscale(1);opacity:.65;margin-inline-end:4px;}
.chev{flex:0 0 36px;height:36px;border:1px solid #e5e7eb;border-radius:50%;display:grid;place-items:center;color:#475569;font-size:1.3rem;line-height:1;transition:transform .2s;}
details[open] .chev{transform:rotate(90deg);}
details.rtl .chev{transform:scaleX(-1);}
details.rtl[open] .chev{transform:scaleX(-1) rotate(90deg);}
.sbody{padding:6px 18px 16px;border-top:1px dashed #e8ebf2;color:#334155;font-size:.9rem;}
.sbody .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px 20px;margin:12px 0;}
.sbody .grid b{display:block;color:#94a3b8;font-size:.72rem;letter-spacing:.04em;}
a.btn{display:inline-block;background:#ef4444;color:#fff !important;padding:8px 18px;border-radius:10px;text-decoration:none;font-weight:700;}
.dl-soon{color:#d97706;font-weight:600;}.dl-exp{color:#9ca3af;text-decoration:line-through;}
.foot{text-align:center;opacity:.75;font-size:.9rem;}
@media(max-width:900px){.feats{grid-template-columns:repeat(2,1fr);}.hero h1{font-size:2rem;}}
@media(max-width:640px){.thumb{flex-basis:84px;height:64px;}.feats{grid-template-columns:1fr;}}
"""

RTL_CSS = """
.stApp, .stApp [data-testid="stMainBlockContainer"], .stApp [data-testid="stVerticalBlock"],
.stApp [data-testid="stHorizontalBlock"], .stApp [data-testid="stMarkdownContainer"],
.stApp [data-testid="stHeading"], .stApp [data-testid="stHeadingWithActionElements"],
.stApp [data-testid="stCaptionContainer"], .stApp [data-testid="stExpander"],
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp p, .stApp label, .stApp li,
[data-testid="stTooltipContent"], [data-testid="stTooltipContent"] *, [data-baseweb="popover"] p{
  direction:rtl !important; text-align:right !important;}
.stApp .hero, .stApp .hero *, .stApp .stat, .stApp .quote, .stApp .foot{text-align:center !important;}
.stApp :not([data-testid="stIconMaterial"]):not([class*="material" i]):not(code):not(pre),
[data-testid="stTooltipContent"] *, [data-baseweb="popover"] *{
  font-family:'Sans',Tahoma,sans-serif !important;}
[data-testid="stTooltipContent"]{padding:.6rem 1rem !important;}
[data-testid="stTooltipContent"] ol, [data-testid="stTooltipContent"] ul{
  list-style-position:inside !important; padding:0 !important; margin:0 !important;}
[data-testid="stTooltipContent"] li{margin:0 0 .4em 0 !important; padding:0 !important;}
"""

st.markdown("<style>" + BASE_CSS + ((_font_css() + RTL_CSS) if RTL else "") + "</style>", unsafe_allow_html=True)

# ============================================================== sidebar
with st.sidebar:
    st.markdown(f'<div class="logo">{CAP.format(s=34)}<span>Dara <span class="accent">Scholarship</span> Agent</span></div>',
                unsafe_allow_html=True)
    page = st.radio("nav", ["search", "saved"], key="nav", label_visibility="collapsed",
                    format_func=lambda v: {"search": "🔍  ", "saved": "🔖  "}[v] + T("nav_" + v))
    with st.expander(T("settings")):
        st.selectbox("🌐 Language / زبان / Dil / اللغة", list(i18n.LANGS), format_func=lambda k: i18n.LANGS[k], key="lang")
        _remember_lang(st.session_state["lang"])
        key = st.text_input(T("api_key"), value=os.getenv("GEMINI_API_KEY", ""), type="password", help=T("api_key_help"))
        nat = st.selectbox(T("nationality"), NATIONALITIES, index=0,
                           format_func=lambda x: T("nat_any") if x.startswith("Any")
                           else T("nat_other") if x.startswith("Other") else x)
        if nat.startswith("Other"):
            nat = st.text_input(T("nat_type"), "")
        model = st.selectbox(T("model"), MODELS)
        st.caption(T("fallback", m=agent.FALLBACK_MODEL))
        if st.button(T("clear")):
            db.clear()
            st.rerun()
    st.markdown(f'<div class="quote">{CAP.format(s=30)}<i>{esc(T("quote_a"))}</i>{esc(T("quote_b"))}</div>',
                unsafe_allow_html=True)


# ============================================================== hero + footer
def hero(items):
    cset = {p for i in items for p in db.country_parts(i["country"]) if p not in ("Any country", "Unknown")}
    present = [l for l in LEVELS[:3] if any(l in i["level"] for i in items)]
    feats = "".join(
        f'<div class="feat"><div class="fi {c}">{ico}</div><div><b>{esc(T(f"feat{n}_t"))}</b><span class="d">{esc(T(f"feat{n}_d"))}</span></div></div>'
        for n, c, ico in ((1, "a", "🔍"), (2, "b", "🌐"), (3, "c", "🎛️"), (4, "d", "🎓")))
    stats = (f'<div class="stat"><b>{len(items)}</b><span>{esc(T("stat_sch"))}</span></div>'
             f'<div class="stat"><b>{len(cset)}</b><span>{esc(T("stat_cnt"))}</span></div>'
             f'<div class="stat"><b class="sm">{esc(" • ".join(lvl(l) for l in present) or "—")}</b><span>{esc(T("stat_lvl"))}</span></div>')
    st.markdown(
        '<div class="hero"><div class="brand">' + CAP.format(s=58)
        + f'<h1>{esc(T("hero_a"))}<span class="accent">{esc(T("hero_accent"))}</span>{esc(T("hero_b"))}</h1></div>'
        + f'<p class="tag">{esc(T("tagline"))}</p><div class="feats">{feats}</div><div class="stats">{stats}</div></div>',
        unsafe_allow_html=True)


def footer():
    st.divider()
    st.markdown(
        f'<div class="foot">© {date.today().year} {esc(T("app_name"))} · {esc(T("footer_website"))}: '
        f'<a href="{SITE_URL}" target="_blank" rel="noopener noreferrer">danieldara.com</a> · {esc(T("footer_support"))}: '
        f'<a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a></div>', unsafe_allow_html=True)


# ============================================================== 1) collect
def render_collect():
    st.subheader(T("sec1"))
    with st.container(border=True):
        tab_a, tab_b = st.tabs([T("tab_import"), T("tab_ai")])
        with tab_a:
            st.caption(T("import_caption"))
            names = list(sources.SITES)
            picked = st.multiselect(T("sources"), names, default=["Scholars4Dev", "ScholarshipTab – Masters"])
            pages = st.slider(T("pages"), 1, 30, 10)
            custom = st.text_input(T("custom_url"), "")
            if st.button(T("import_btn"), type="primary"):
                targets = [(n, sources.SITES[n]) for n in picked]
                if custom.strip():
                    targets.append(("Custom", {"url": custom.strip(), "kind": sources.guess_kind(custom)}))
                if not targets:
                    st.warning(T("no_site"))
                else:
                    with st.status(T("importing"), expanded=True) as stt:
                        total = 0
                        for name, cfg in targets:
                            try:
                                found = sources.crawl(
                                    cfg["url"], cfg.get("kind"), pages, cfg.get("level"), cfg.get("country"),
                                    cfg.get("funding"),
                                    progress=lambda p, t_, n, name=name: stt.write(
                                        T("page_progress", site=name, p=p, t=t_, n=n)))
                                db.save(found)
                                total += len(found)
                            except Exception as e:
                                code = getattr(getattr(e, "response", None), "status_code", None)
                                if code in (401, 403, 429):
                                    stt.write(T("site_blocked", site=name, code=code))
                                else:
                                    stt.write(T("site_failed", site=name, e=e))
                        stt.update(label=T("imported", n=total), state="complete")
        with tab_b:
            st.caption(T("ai_caption"))
            c1, c2, c3 = st.columns(3)
            levels = c1.multiselect(T("level"), LEVELS, default=["Master"], format_func=lvl)
            countries_txt = c2.text_input(T("countries"), "")
            field = c3.text_input(T("field"), "")
            c4, c5 = st.columns(2)
            funding = c4.selectbox(T("funding"), ["Any"] + FUNDING[:3], format_func=fund)
            deep = c5.checkbox(T("deep"), True)
            if st.button(T("find_btn"), type="primary"):
                if not key:
                    st.error(T("enter_key"))
                else:
                    with st.status(T("searching"), expanded=True) as stt:
                        try:
                            found = agent.search_scholarships(
                                key, levels, [x.strip() for x in countries_txt.split(",") if x.strip()],
                                field, nat, "" if funding == "Any" else funding,
                                deep=deep, model=model, out_lang=AI_LANG, log=stt.write)
                            db.save(found)
                            stt.update(label=T("found_saved", n=len(found)), state="complete")
                        except Exception as e:
                            stt.update(label=T("search_failed"), state="error")
                            st.error(T("error", e=e))


# ============================================================== 2) browse
def card_html(i):
    code = countries.code_for(i["country"])
    ft = i.get("funding_type") or "Unknown"
    dl_cls, dl_txt = "", i.get("deadline_text") or i.get("deadline") or ""
    if i.get("deadline"):
        try:
            days = (date.fromisoformat(i["deadline"]) - date.today()).days
            dl_cls = "dl-exp" if days < 0 else ("dl-soon" if days <= 30 else "")
        except ValueError:
            pass
    ic = lambda e: f'<span class="ic">{e}</span>'
    meta = [ic("📍") + esc(i["country"]), ic("🎓") + esc(", ".join(lvl(l) for l in i["level"])),
            ic("💰") + esc(i18n.label(lang, "chip", ft))]
    if dl_txt:
        meta.append(ic("📅") + f'<span class="{dl_cls}">{esc(str(dl_txt)[:34])}</span>')
    url = i.get("url", "")
    href = url if url.startswith(("http://", "https://")) else "#"
    cell = lambda k, v: f'<div><b>{esc(T(k)).upper()}</b>{esc(v) or "-"}</div>'
    body = (f'<p style="margin:10px 0 0">{esc(i.get("summary", ""))}</p><div class="grid">'
            + cell("university", i.get("university")) + cell("fields", ", ".join(i.get("fields") or []))
            + cell("amount", i.get("amount")) + cell("deadline", dl_txt or T("unknown"))
            + cell("eligible", ", ".join(i.get("eligible_nationalities") or [])) + cell("language", i.get("language_requirement"))
            + cell("source", i.get("source", "ai-search")) + '</div>'
            + f'<a class="btn" href="{esc(href)}" target="_blank" rel="noopener noreferrer">{esc(T("official"))} ↗</a>')
    return (f'<details class="sch{" rtl" if RTL else ""}"><summary><div class="thumb c-{code}"></div>'
            f'<div class="info"><div class="ttl">{esc(i["title"])}</div><div class="meta">'
            + "".join(f"<span>{m}</span>" for m in meta)
            + f'</div></div><div class="chev">›</div></summary><div class="sbody">{body}</div></details>')


def _more(k):
    st.session_state[k] = st.session_state.get(k, PAGE_SIZE) + PAGE_SIZE


def render_browse(items):
    st.subheader(T("sec2"))
    if not items:
        st.info(T("nothing"))
        return
    f1, f2, f3, f4 = st.columns(4)
    all_countries = sorted({p for i in items for p in db.country_parts(i["country"])})
    sel_levels = f1.multiselect(T("f_level"), LEVELS, default=LEVELS, format_func=lvl)
    sel_countries = f2.multiselect(T("f_country"), all_countries, default=all_countries)
    sel_funding = f3.multiselect(T("f_funding"), FUNDING, default=FUNDING, format_func=fund)
    text = f4.text_input(T("f_keyword"))
    g1, g2 = st.columns(2)
    only_open = g1.checkbox(T("hide_expired"), True)
    nat_label = T("nat_any") if nat.startswith("Any") else nat
    only_nat = g2.checkbox(T("only_nat", nat=nat_label), True)

    def keep(i):
        if not set(i["level"]) & set(sel_levels):
            return False
        if not set(db.country_parts(i["country"])) & set(sel_countries):
            return False
        if i.get("funding_type", "Unknown") not in sel_funding:
            return False
        if only_open and not db.is_open(i):
            return False
        if only_nat and not db.nationality_ok(i, nat):
            return False
        hay = " ".join(i.get("fields") or []) + i["title"] + i.get("summary", "") + (i.get("university") or "")
        return not text or text.lower() in hay.lower()

    shown = [i for i in items if keep(i)]
    st.write(T("results_count", n=len(shown), total=len(items)))

    todo = [i for i in shown if db.needs_enrich(i)]
    if todo:
        with st.expander(T("enrich_exp", n=len(todo))):
            top = min(len(todo), 100)
            n_max = st.slider(T("enrich_howmany"), 1, top, min(top, 20)) if top > 1 else 1
            if st.button(T("enrich_btn")):
                if not key:
                    st.error(T("enter_key"))
                else:
                    with st.status(T("enrich_status"), expanded=True) as stt:
                        try:
                            done = agent.enrich(key, todo[:n_max], model=model, out_lang=AI_LANG, log=stt.write)
                            db.save(done)
                            stt.update(label=T("enriched", n=len(done)), state="complete")
                            st.rerun()
                        except Exception as e:
                            stt.update(label=T("failed"), state="error")
                            st.error(T("error", e=e))

    lvls = [l for l in LEVELS if l in sel_levels]
    if not shown or not lvls:
        st.info(T("no_results"))
    else:
        st.markdown("<style>" + countries.css_for({countries.code_for(i["country"]) for i in shown} | {"globe"}) + "</style>",
                    unsafe_allow_html=True)
        tabs = st.tabs([f"{lvl(l)} ({sum(l in x['level'] for x in shown)})" for l in lvls])
        for tab, l in zip(tabs, lvls):
            with tab:
                rows = [x for x in shown if l in x["level"]]
                k = f"n_{l}"
                n = st.session_state.get(k, PAGE_SIZE)
                if rows:
                    st.markdown("".join(card_html(x) for x in rows[:n]), unsafe_allow_html=True)
                if len(rows) > n:
                    st.button(f"{T('load_more')} ({len(rows) - n})", key=f"more_{l}", on_click=_more, args=(k,))

    if shown:
        df = pd.DataFrame(shown)
        for col in ("level", "fields", "eligible_nationalities"):
            if col in df:
                df[col] = df[col].apply(lambda v: ", ".join(v) if isinstance(v, list) else v)
        st.download_button(T("export"), df.to_csv(index=False).encode("utf-8-sig"), "scholarships.csv", "text/csv")
    st.caption(T("verify"))


# ============================================================== page
all_items = db.all_items()
hero(all_items)
if page == "search":
    render_collect()
render_browse(all_items)
footer()
