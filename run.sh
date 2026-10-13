#!/usr/bin/env bash
# One-click launcher for macOS / Linux:  bash run.sh
set -e
cd "$(dirname "$0")"

PY="${PYTHON:-python3}"
if ! command -v "$PY" >/dev/null 2>&1; then
  echo "Python 3.10+ is required. Install it from https://www.python.org/downloads/"; exit 1
fi

[ -d venv ] || { echo "Creating virtual environment..."; "$PY" -m venv venv; }
# shellcheck disable=SC1091
source venv/bin/activate

echo "Checking dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

[ -f .env ] || { cp .env.example .env; echo "Created .env (add your GEMINI_API_KEY there or in the app sidebar)."; }

# skip Streamlit's first-run "enter your email" prompt
mkdir -p "$HOME/.streamlit"
[ -f "$HOME/.streamlit/credentials.toml" ] || printf '[general]\nemail = ""\n' > "$HOME/.streamlit/credentials.toml"

streamlit run app.py
