"""Local persistence: UI settings (settings.json) and the Gemini API key (.env).
Both files are listed in .gitignore, so they are never committed to GitHub."""
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).parent
SETTINGS_FILE = ROOT / "settings.json"
ENV_FILE = ROOT / ".env"


def load_settings():
    try:
        data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_settings(values):
    """Merge `values` into settings.json (written only when something changed)."""
    current = load_settings()
    merged = {**current, **values}
    if merged == current:
        return
    try:
        SETTINGS_FILE.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError:
        pass


def save_env_value(name, value):
    """Set (or, with value=None, remove) NAME in .env, keeping every other line untouched."""
    lines = ENV_FILE.read_text(encoding="utf-8").splitlines() if ENV_FILE.exists() else []
    out, done = [], False
    for line in lines:
        if re.match(rf"\s*{re.escape(name)}\s*=", line):
            if value is not None and not done:
                out.append(_env_line(name, value))
                done = True
            continue                       # drop old / duplicate lines
        out.append(line)
    if value is not None and not done:
        out.append(_env_line(name, value))
    ENV_FILE.write_text("\n".join(out) + "\n", encoding="utf-8")
    if value is None:
        os.environ.pop(name, None)
    else:
        os.environ[name] = _clean(value)


def _clean(value):
    return str(value).replace("\r", "").replace("\n", "").strip()


def _env_line(name, value):
    v = _clean(value)
    if not re.fullmatch(r"[A-Za-z0-9_.\-]+", v):
        v = '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return f"{name}={v}"


def can_save_key():
    """Saving the key to disk is only safe when the app runs on the user's own computer.
    On a shared / public server it would leak one visitor's key to the others.
    Override with DARA_SAVE_KEY=1 (always allow) or DARA_SAVE_KEY=0 (never)."""
    flag = os.getenv("DARA_SAVE_KEY", "").strip().lower()
    if flag in ("1", "true", "yes"):
        return True
    if flag in ("0", "false", "no"):
        return False
    try:
        import streamlit as st
        host = (st.context.headers.get("Host") or "").lower()
    except Exception:
        return False
    return re.sub(r":\d+$", "", host) in ("localhost", "127.0.0.1", "[::1]")
