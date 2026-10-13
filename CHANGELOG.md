# Changelog

All notable changes to **Dara Scholarship Agent** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/idanieldara/scholarship-agent/compare/v0.5.0...HEAD
[0.5.0]: https://github.com/idanieldara/scholarship-agent/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/idanieldara/scholarship-agent/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/idanieldara/scholarship-agent/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/idanieldara/scholarship-agent/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/idanieldara/scholarship-agent/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/idanieldara/scholarship-agent/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/idanieldara/scholarship-agent/releases/tag/v0.1.0
