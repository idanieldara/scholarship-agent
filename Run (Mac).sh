#!/usr/bin/env bash
# One-click launcher for macOS / Linux:  bash "Run (Mac).sh"
set -e
cd "$(dirname "$0")"

# make sure the whole project is here (not just this script)
if [ ! -f app.py ] || [ ! -f requirements.txt ]; then
  echo
  echo "Project files (app.py / requirements.txt) not found in: $(pwd)"
  echo "Extract the whole ZIP (or clone the repository) and run this script from inside the project folder."
  echo "Do not move the script out of the project folder."
  exit 1
fi

OK_PY='import sys; sys.exit(0 if (3, 10) <= sys.version_info[:2] <= (3, 14) else 1)'

# pick a supported Python (3.10 - 3.14); 3.12 / 3.13 are preferred
pick_python() {
  for c in "${PYTHON:-}" python3.13 python3.12 python3.11 python3.14 python3.10 python3 python; do
    [ -n "$c" ] || continue
    command -v "$c" >/dev/null 2>&1 || continue
    if "$c" -c "$OK_PY" >/dev/null 2>&1; then echo "$c"; return 0; fi
  done
  return 1
}

PY="$(pick_python)" || {
  echo
  echo "No supported Python found. This app needs Python 3.10 - 3.14 (3.12 or 3.13 recommended)."
  echo "Very new versions (for example 3.15) have no pre-built packages yet (pyarrow, pyyaml) and fail to install."
  echo "Download Python 3.13 from https://www.python.org/downloads/"
  exit 1
}

# an old venv built with an unsupported Python must be recreated
if [ -x venv/bin/python ] && ! venv/bin/python -c "$OK_PY" >/dev/null 2>&1; then
  echo "Existing virtual environment uses an unsupported Python - recreating it..."
  rm -rf venv
fi

[ -d venv ] || { echo "Creating virtual environment with $PY..."; "$PY" -m venv venv; }
# shellcheck disable=SC1091
source venv/bin/activate

echo "Checking dependencies..."
pip install -q --upgrade pip || true
if ! pip install -q -r requirements.txt; then
  echo
  echo "Installing the dependencies failed (see the message above)."
  echo "If it mentions a compiler or 'Failed building wheel', use Python 3.12 or 3.13, delete the 'venv' folder and run this script again."
  exit 1
fi

[ -f .env ] || { cp .env.example .env; echo "Created .env (add your GEMINI_API_KEY there or in the app sidebar)."; }

# skip Streamlit's first-run "enter your email" prompt
mkdir -p "$HOME/.streamlit"
[ -f "$HOME/.streamlit/credentials.toml" ] || printf '[general]\nemail = ""\n' > "$HOME/.streamlit/credentials.toml"

streamlit run app.py
