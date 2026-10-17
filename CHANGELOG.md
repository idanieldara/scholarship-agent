# Changelog

All notable changes to **Dara Scholarship Agent** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.6.0] - 2026-10-16

### Added
- **Saved API key**: the Gemini key typed in the sidebar is written to the local `.env` file and pre-filled after a refresh or restart. It is only saved when the app is opened on this computer (`localhost`); on a server it stays in the browser session and never touches the disk. A *Remember the key on this computer* checkbox and a *Forget saved key* button give you control, and `DARA_SAVE_KEY=1|0` overrides the automatic detection.
- Nationality and Gemini model are remembered in `settings.json`, together with the language.
- **Get a free API key ↗** button under the key field (opens Google AI Studio in a new tab). The link inside the help tooltip is now a real Markdown link.
- **Duplicate merging**: the same scholarship found on several websites or by the AI search (matched by link and by normalised title) is stored once, with countries, sources and data combined. Duplicates left in an existing database are merged automatically when the app starts.
- **Re-import refreshes the list**: importing again adds new scholarships, refreshes changed deadlines, and keeps funding / eligibility data that AI enrichment filled in.
- **NEW** badge for scholarships added in the last 3 days; the newest additions are listed first.
- Import and AI search report how many results were new, updated or already up to date.
- The AI search receives the titles you already saved and is asked to find different scholarships.
- `storage.py` (settings and API-key persistence) and the optional `DARA_SAVE_KEY` setting.

### Changed
- Saving results merges records instead of replacing the one with the same title and country.
- The SQLite file is created next to the app files, whichever folder the app is started from.

### Fixed
- The API key had to be typed again after every refresh or browser restart.
- The link in the API-key help tooltip could not be clicked.
- The same scholarship was listed several times when it came from different sources.
- Importing a website again overwrote funding and eligibility data filled in by AI enrichment.

## [0.5.3] - 2026-10-14

### Fixed
- Running a launcher outside the project folder (for example from inside the ZIP without extracting, or after moving the file) ended with pip's "Could not open requirements file" and then "'streamlit' is not recognized". `Run (Windows).bat` and `Run (Mac).sh` now check that `app.py` and `requirements.txt` are next to them and stop with a clear explanation if not.

### Changed
- README troubleshooting (English, Persian, Turkish) covers this error.

## [0.5.2] - 2026-10-13

### Changed
- Launcher scripts renamed to be self-explanatory: `run.bat` is now **`Run (Windows).bat`** and `run.sh` is now **`Run (Mac).sh`** (it also works on Linux). Start the macOS / Linux launcher with `bash "Run (Mac).sh"`; the quotes are required because the name contains spaces and parentheses.
- README (English, Persian, Turkish) updated with the new file names.

## [0.5.1] - 2026-10-13

### Fixed
- Installation failed on very new Python versions (for example 3.15). Dependencies such as `pyarrow` and `pyyaml` have no pre-built packages for them yet, so pip tried to compile them and stopped with "Microsoft Visual C++ 14.0 or greater is required". `run.bat` and `run.sh` now pick a supported Python (3.10 – 3.14, preferring 3.12 / 3.13) automatically, even when a newer one is installed.
- A virtual environment created with an unsupported Python is detected and recreated.
- The launchers now stop with a clear message when installing the dependencies fails, instead of continuing and ending with "'streamlit' is not recognized".

### Changed
- README documents the supported Python range (3.10 – 3.14, 3.12 / 3.13 recommended) and has new troubleshooting entries for compiler and "Failed building wheel" errors.

## [0.5.0] - 2026-10-12

### Added
- One-click launchers: `run.bat` (Windows) and `run.sh` (macOS / Linux). They create the virtual environment, install or update dependencies, create `.env` from `.env.example`, skip Streamlit's first-run email prompt, and start the app.
- Two documented installation methods in the README: **direct download (no Git)** and **with Git**, including how to update with each.
- README section explaining how to use the launcher scripts, with notes for common problems.

### Changed
- Project structure in the README now lists the launcher scripts.

## [0.4.1] - 2026-10-10

### Added
- Turkish README (`README.tr.md`).
- Clickable table of contents and a language switcher (English · فارسی · Türkçe) in every README.
- `CHANGELOG.md` (this file).

### Changed
- README sections use explicit HTML anchors so table-of-contents links work reliably on GitHub.
- README usage steps updated for the new sidebar **Settings** and navigation.

## [0.4.0] - 2026-10-10

### Added
- **Dashboard redesign** inspired by the project mockup: hero header with accent title, four feature cards, live statistics (scholarships, countries, levels), and pill-style tabs and buttons.
- **Sidebar navigation** with *Search scholarships* and *Saved results* pages, a *Settings* section (language, API key, nationality, model, clear data) and an inspirational quote card.
- **Expandable scholarship cards** with a thumbnail, location / level / funding / deadline chips, a details grid and an *Official page* button. Deadlines are highlighted when they are soon or expired.
- **Landmark illustration for every destination country** (39 countries plus a globe fallback), for example the Eiffel Tower for France, Big Ben for the UK and the Brandenburg Gate for Germany. Add `assets/countries/<code>.jpg|png|webp` to use your own photo instead.
- `countries.py` (country name → thumbnail) and `tools/make_country_art.py` (regenerates the SVG illustrations).
- "Show more" pagination (30 results at a time per level tab).
- Streamlit theme and minimal toolbar in `.streamlit/config.toml`.
- Localized hero text, statistics, funding chips and quote in English, Persian, Turkish and Arabic.

### Changed
- Results are rendered as HTML cards instead of Streamlit expanders (faster with hundreds of results).
- Settings moved into a sidebar section so they stay available on every page.

### Security
- All scraped or AI-generated text is HTML-escaped before display, and links are limited to `http(s)`.

## [0.3.1] - 2026-10-10

### Added
- Professional English and Persian README with badges, architecture diagram, configuration table, deployment guide and troubleshooting.
- MIT `LICENSE`, a `.gitignore` that keeps `.env`, the local database and settings out of Git, and a project banner (`docs/screenshots/banner.png`).

## [0.3.0] - 2026-10-09

### Added
- **Four interface languages**: English, Persian, Turkish and Arabic, with full right-to-left layout for Persian and Arabic.
- IRANSansX font for Persian and Arabic, embedded in the page so it works without any server configuration.
- AI-generated summaries are written in the selected interface language.
- The chosen language survives a page refresh (`?lang=` in the URL plus a local `settings.json`).
- Localized application name and a step-by-step "How to get a Gemini API key" tooltip in all four languages.
- Footer with the website (danieldara.com) and support email.
- Friendly "site refused automated access" message for HTTP 401 / 403 / 429 responses.

### Changed
- Application name is now **Dara Scholarship Agent**.
- Funding is shown next to a scholarship only when it is known, and mixed-direction text is isolated so Persian and English titles no longer scramble.

### Fixed
- Leftover strip when the sidebar was collapsed.
- Numbered steps in the API-key tooltip overflowing the box in right-to-left mode.
- Persian headings and captions not aligning to the right.
- Crash of the enrichment slider when exactly one result was left to enrich.

## [0.2.0] - 2026-10-09

### Added
- **Website import without AI or API key**: Scholars4Dev, ScholarshipTab (Masters, PhD, MBA, Undergraduate, Postgraduate, Fellowship, Fully funded), ScholarshipSet (Africa) and country sites for Germany, the UK, Canada, the USA and Australia. Custom category URLs are supported, and pagination is detected automatically.
- **Deep search**: leaving *Destination countries* empty searches all countries, with one Gemini search pass per world region.
- **AI enrichment**: Gemini reads each scholarship page (URL context) and fills funding, amount, eligible nationalities, fields and language requirements.
- Gemini model selector in the sidebar and a configurable fallback model (`GEMINI_FALLBACK_MODEL`).
- Automatic retries (3, 6, 12 and 24 seconds) on temporary `503` errors.
- Multi-country filter: scholarships listing several countries are matched per country.

### Changed
- Default model is `gemini-2.5-flash` with `gemini-2.5-flash-lite` as fallback (`gemini-3-flash-preview` hit quota errors on the free tier).
- Quota errors (`429`) no longer wait and retry; the app switches to the fallback model immediately and shows the full error text.
- A 5-second pause between search passes to stay within per-minute rate limits.
- Requests use standard browser-like headers.
- Scholarships with unknown eligibility are kept when filtering by nationality, so opportunities are not hidden by missing data.
- Removed the "Extra notes" search field.

### Fixed
- Countries parsed as "." are now stored as "Unknown".

## [0.1.0] - 2026-10-09

### Added
- First release: a Streamlit app that uses Gemini with Google Search grounding to find scholarships and converts the result to structured JSON.
- Scholarships listed by education level (Bachelor, Master, PhD, Postdoc, Other).
- Filters for country, field of study, funding type, deadline and a selectable nationality (not limited to one country).
- Local SQLite storage, CSV export and a local-first setup that runs on your own computer.

[Unreleased]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/compare/v0.5.3...v0.6.0
[0.5.3]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/compare/v0.5.2...v0.5.3
[0.5.2]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/compare/v0.5.1...v0.5.2
[0.5.1]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/YOUR_USERNAME/dara-scholarship-agent/releases/tag/v0.1.0
