<div align="center">

<img src="assets/screenshots/banner.jpg" alt="Dara Scholarship Agent: AI scholarship finder powered by Google Gemini, built with Python and Streamlit" width="860">

<br />

# 🎓 Dara Scholarship Agent

**A free, open-source AI scholarship finder. Search, filter and compare scholarships worldwide by degree level, destination country, field of study, funding type and your own nationality.**

Powered by **Google Gemini** · Built with **Python & Streamlit** · UI in **English · فارسی · Türkçe · العربية**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B?logo=streamlit&logoColor=white)
![Gemini API](https://img.shields.io/badge/Google%20Gemini-API-4285F4?logo=googlegemini&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

[Features](#features) · [Quick start](#quick-start) · [Usage](#usage) · [Deploy online](#deploy) · [Troubleshooting](#troubleshooting)

🌐 **English** · [فارسی](README.fa.md) · [Türkçe](README.tr.md)

</div>

---

<details open>
<summary><b>📑 Table of contents</b></summary>

- [📖 What is Dara Scholarship Agent?](#what-is)
- [✨ Features](#features)
- [🧠 How it works](#how-it-works)
- [🚀 Quick start](#quick-start)
  - [🔑 Get a free Gemini API key](#api-key)
  - [⚙️ Configuration](#configuration)
- [🧭 Usage](#usage)
- [🌐 Supported sources](#sources)
- [🗂️ Project structure](#project-structure)
- [🖼️ Country images](#country-images)
- [☁️ Deploy online](#deploy)
- [🛠️ Troubleshooting](#troubleshooting)
- [⚠️ Responsible use & disclaimer](#responsible-use)
- [🗺️ Roadmap](#roadmap)
- [🤝 Contributing](#contributing)
- [📄 License](#license)
- [👤 Author & support](#author)

</details>

---

<a id="what-is"></a>

## 📖 What is Dara Scholarship Agent?

Finding a **fully funded scholarship** means opening dozens of websites, each with its own layout, deadlines and eligibility rules.
**Dara Scholarship Agent** is a **scholarship search engine and AI agent** that does the legwork for you:

1. it **imports hundreds of scholarships** from popular scholarship websites in seconds (no AI, no API key needed),
2. it can **search the live web with Gemini + Google Search** to discover scholarships those sites do not list,
3. it **reads each scholarship page with AI** to fill in funding, eligible nationalities, fields of study and language requirements,
4. and it lets you **filter everything instantly** by degree level, country, field, funding, deadline and **your nationality**, all stored locally on your computer.

It is built for students applying for **Bachelor, Master, PhD and Postdoc** scholarships abroad, and for study-abroad consultants who need a fast, repeatable way to build shortlists.

<a id="features"></a>

## ✨ Features

- 🎨 **Modern dashboard UI**: hero header, sidebar navigation, live statistics, expandable scholarship cards, and a **landmark illustration for every destination country** (Eiffel Tower for France, Big Ben for the UK, Brandenburg Gate for Germany, and 35+ more).
- 🌍 **Scholarships by education level**: separate tabs for Bachelor, Master, PhD, Postdoc and Other.
- 🔎 **Powerful filters**: country, field or keyword, funding type (Full / Partial / Tuition only), hide expired deadlines, and **eligibility by nationality** (choose any country, or "Any").
- 📚 **Fast website import (no AI, no key)**: Scholars4Dev, ScholarshipTab, ScholarshipSet, and country sites for Germany, the UK, Canada, the USA and Australia. Paste any compatible category URL to add more.
- 🤖 **AI web search**: Gemini + Google Search grounding. Leave *Destination countries* empty to search **all countries**; a deep-search mode runs one pass per world region.
- ✨ **AI enrichment**: Gemini reads each scholarship page (URL context) and fills funding, amount, eligible nationalities, fields and language requirements.
- 🗣️ **Four interface languages** with full **RTL support** (Persian and Arabic) and the *Sans* font. Summaries are written in your chosen language, and your choice survives a page refresh.
- 💾 **Local-first**: results are saved in a local SQLite database. Filtering is instant and costs no API calls.
- ⬇️ **Export to CSV** for Excel and Google Sheets.
- 🛡️ **Reliable by design**: automatic retries for overloaded models (503), fast fallback on quota errors (429), and a configurable fallback model.
- 🔐 **Private**: your API key stays on your machine (`.env` or the sidebar field).

<!--
## 🖼️ Screenshots

| English | فارسی (RTL) |
|---|---|
| ![Dashboard in English](assets/screenshots/app-en.png) | ![Persian RTL dashboard](assets/screenshots/app-fa.png) |
-->

<a id="how-it-works"></a>

## 🧠 How it works

```mermaid
flowchart LR
    A[Scholarship websites] -->|crawler| D[(Local SQLite)]
    B[Gemini + Google Search] -->|AI web search| D
    D -->|URL context| C[AI enrichment]
    C --> D
    D --> E[Filters: level, country, field, funding, deadline, nationality]
    E --> F[Streamlit UI: EN, FA, TR, AR + CSV export]
```

<a id="quick-start"></a>

## 🚀 Quick start

**Requirements:** Python 3.10 or newer and a free Gemini API key (only needed for AI features).

```bash
# 1. get the code
git clone https://github.com/idanieldara/scholarship-agent.git
cd dara-scholarship-agent

# 2. create a virtual environment
python -m venv venv
venv\Scripts\activate            # Windows
# source venv/bin/activate       # macOS / Linux

# 3. install dependencies
pip install -r requirements.txt

# 4. add your API key
copy .env.example .env           # Windows
# cp .env.example .env           # macOS / Linux

# 5. run
streamlit run app.py
```

The app opens at **http://localhost:8501**. Run it from the project folder.

<a id="api-key"></a>

### 🔑 Get a free Gemini API key

1. Go to <https://aistudio.google.com/api-keys>.
2. Sign in with your Google account (`@gmail.com`). If you do not have one, you will be asked to create one.
3. Click **Create API key**.
4. Enter a name for the key and click **Create key**.
5. Click the key's name under the **Key** column, copy the key, and paste it into `.env` (`GEMINI_API_KEY=...`) or into the sidebar field of the app.

> The website import tab works **without** any API key.

<a id="configuration"></a>

### ⚙️ Configuration

| Variable | Default | Description |
|---|---|---|
| `GEMINI_API_KEY` | none | Your Google AI Studio key (or type it in the sidebar). |
| `GEMINI_MODEL` | `gemini-2.5-flash` | Main model. Can also be changed in the sidebar. |
| `GEMINI_FALLBACK_MODEL` | `gemini-2.5-flash-lite` | Used automatically when the main model is overloaded or out of quota. |

<a id="usage"></a>

## 🧭 Usage

1. Open **Settings** in the sidebar to choose your language, nationality, Gemini model and API key (pick *Any* nationality to see everything). Use the sidebar menu to switch between **Search scholarships** and **Saved results**.
2. **Collect scholarships**
   - *Import from websites*: select sources, set max pages, click **Import**.
   - *AI web search*: choose level, countries (empty = all), field and funding, then click **Find scholarships with AI**.
3. **Browse & filter**: use the level tabs and filters. Unknown eligibility rules are kept so you do not miss opportunities.
4. **Enrich with AI** (optional): let Gemini read the pages of results that lack funding or nationality info.
5. **Export CSV** and verify every deadline on the official page before applying.

<a id="sources"></a>

## 🌐 Supported sources

| Source | Content |
|---|---|
| Scholars4Dev | International scholarships (all levels) |
| ScholarshipTab | Masters, PhD, MBA, Undergraduate, Postgraduate, Fellowship, Fully funded |
| ScholarshipSet (Africa) | Masters, PhD, Undergraduate |
| GermanyScholarships · UKScholarships · ScholarshipCA · UScholarships · ScholarshipAU | Country-specific scholarships |
| Custom URL | Any category page with a compatible layout |
| Gemini + Google Search | Anything else on the open web |

> Some websites may refuse automated access (HTTP 403). The app skips them with a clear message; use the AI search tab instead.

<a id="project-structure"></a>

## 🗂️ Project structure

```text
dara-scholarship-agent/
├── app.py              # Streamlit UI, filters, language and RTL handling
├── agent.py            # Gemini agent: web search, enrichment, retries and fallback
├── sources.py          # Website crawlers (no AI) and date/level parsing
├── db.py               # Local SQLite storage and filtering helpers
├── i18n.py             # EN / FA / TR / AR translations
├── countries.py        # country name -> landmark thumbnail (SVG or your own photo)
├── assets/countries/   # landmark illustrations (de.svg, fr.svg, ...) + optional photos
├── tools/make_country_art.py  # regenerates the SVG illustrations
├── static/             # Sans fonts used for Persian and Arabic
├── assets/screenshots/   # README images
├── requirements.txt
├── .env.example
└── LICENSE
```

<a id="country-images"></a>

## 🖼️ Country images

Every scholarship card shows a thumbnail of a famous landmark of its destination country (Eiffel Tower, Big Ben, Brandenburg Gate, Sydney Opera House, Mount Fuji, and more). Scholarships without a specific country get a globe.

To use **your own photos** instead of the bundled illustrations, drop a file named after the two-letter country code into `assets/countries/`:

```text
assets/countries/de.jpg     # Germany
assets/countries/gb.webp    # United Kingdom
assets/countries/us.png     # United States
```

Supported formats: `.jpg`, `.png`, `.webp` (a photo always wins over the `.svg`). Only use images you own or that are licensed for reuse. Restart the app to see the change. To add a new country, add its names to `NAMES` in `countries.py` and put `<code>.jpg` (or `.svg`) in the same folder.

<a id="deploy"></a>

## ☁️ Deploy online

GitHub stores your code; it does not run Streamlit apps. To make the app available online:

- **Streamlit Community Cloud (free):** push the repo to GitHub, open <share.streamlit.io>, click **Create app**, choose the repo, branch `main` and file `app.py`, then **Deploy**.
  Do **not** add your own API key to *Secrets* on a public app (anyone could spend your quota); leave it empty so each visitor enters their own key in the sidebar. Saved results reset when the app restarts.
- **Your own server (VPS):** `pip install -r requirements.txt`, then `streamlit run app.py --server.port 8501 --server.address 0.0.0.0` behind Nginx/Caddy with HTTPS.

<a id="troubleshooting"></a>

## 🛠️ Troubleshooting

| Problem | Meaning and fix |
|---|---|
| `429` / `RESOURCE_EXHAUSTED` | Quota or rate limit reached. The app switches to the fallback model; reduce passes (turn off *Deep search*), wait a minute, or enable billing. |
| `503 UNAVAILABLE` | Model overloaded. The app retries automatically (3, 6, 12, 24 s) and then uses the fallback model. |
| `403 Forbidden` for a website | That site blocks automated access. Use another source or the AI search tab. |
| Persian font not applied | Keep `static/Sans-Regular.woff2` and `static/Sans-Bold.woff2` next to `app.py` and restart the app. |
| Few AI results | Gemini is not a crawler. Use website import for volume, and AI search for discovery. |

<a id="responsible-use"></a>

## ⚠️ Responsible use & disclaimer

- Scholarship information can be incomplete or outdated, and AI can make mistakes. **Always verify deadlines, eligibility and requirements on the official page.**
- The crawlers are intended for light, personal use. Respect each website's terms of service and `robots.txt`, and keep the page limits modest.
- The font files in `static/` are *Sans*; check its license before redistributing a fork. If the files are missing the app falls back to Tahoma.

<a id="roadmap"></a>

## 🗺️ Roadmap

- [ ] More scholarship sources and an official-site connector for DAAD, Chevening, Fulbright
- [ ] Deadline reminders by email / WhatsApp / Telegram
- [ ] Saved searches and favorites
- [ ] Docker image and one-click deploy

<a id="contributing"></a>

## 🤝 Contributing

Issues and pull requests are welcome. Please open an issue first for larger changes, keep code formatted, and add translations for new UI text to all four languages in `i18n.py`.

<a id="license"></a>

## 📄 License

Released under the [MIT License](LICENSE).

<a id="author"></a>

## 👤 Author & support

Built by **Daniel Dara**, web developer and AI automation builder.

- 🌐 Website: [danieldara.com](https://danieldara.com)

If this project helps you, please give it a ⭐ on GitHub.

<details>
<summary>Topics</summary>

scholarship finder · scholarship search engine · fully funded scholarships · study abroad · master's scholarships · PhD scholarships · AI agent · Google Gemini API · Streamlit app · Python web scraper · RTL Persian Arabic Turkish UI

</details>
"# scholarship-agent" 
