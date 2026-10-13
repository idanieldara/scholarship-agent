@echo off
rem One-click launcher for Windows: double-click run.bat
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
  echo Python 3.10+ is required. Install it from https://www.python.org/downloads/ ^(tick "Add Python to PATH"^).
  pause
  exit /b 1
)

if not exist venv (
  echo Creating virtual environment...
  python -m venv venv
)
call venv\Scripts\activate

echo Checking dependencies...
python -m pip install -q --upgrade pip
pip install -q -r requirements.txt

if not exist .env (
  copy .env.example .env >nul
  echo Created .env ^(add your GEMINI_API_KEY there or in the app sidebar^).
)

rem skip Streamlit's first-run "enter your email" prompt
if not exist "%USERPROFILE%\.streamlit\credentials.toml" (
  if not exist "%USERPROFILE%\.streamlit" mkdir "%USERPROFILE%\.streamlit"
  echo [general]> "%USERPROFILE%\.streamlit\credentials.toml"
  echo email = "">> "%USERPROFILE%\.streamlit\credentials.toml"
)

streamlit run app.py
pause
