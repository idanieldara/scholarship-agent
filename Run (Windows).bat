@echo off
rem One-click launcher for Windows: double-click Run (Windows).bat
setlocal
cd /d "%~dp0"

rem ---- make sure the whole project is here (not just this file) ----
set "MISSING="
if not exist app.py set "MISSING=1"
if not exist requirements.txt set "MISSING=1"
if defined MISSING (
  echo.
  echo Project files ^(app.py / requirements.txt^) not found in this folder:
  echo   %CD%
  echo.
  echo Extract the WHOLE zip first ^(right-click the zip, then Extract All^),
  echo and run this file from inside the extracted project folder.
  echo Do not run it from inside the zip and do not move it out of the project folder.
  echo If you use GitHub, check that app.py and requirements.txt exist in the repository.
  pause
  exit /b 1
)

rem ---- pick a supported Python (3.10 - 3.14); 3.12 / 3.13 are preferred ----
set "PYCMD="
for %%V in (3.13 3.12 3.11 3.14 3.10) do (
  if not defined PYCMD (
    py -%%V -c "import sys" >nul 2>nul && set "PYCMD=py -%%V"
  )
)
if not defined PYCMD (
  python -c "import sys; sys.exit(0 if (3,10) <= sys.version_info[:2] <= (3,14) else 1)" >nul 2>nul && set "PYCMD=python"
)
if not defined PYCMD (
  echo.
  echo No supported Python found. This app needs Python 3.10 - 3.14 ^(3.12 or 3.13 recommended^).
  echo Very new versions ^(for example 3.15^) have no pre-built packages yet ^(pyarrow, pyyaml^) and fail to install.
  echo Download Python 3.13 from https://www.python.org/downloads/windows/ and tick "Add Python to PATH".
  pause
  exit /b 1
)

rem ---- an old venv built with an unsupported Python must be recreated ----
if exist venv\Scripts\python.exe (
  venv\Scripts\python.exe -c "import sys; sys.exit(0 if (3,10) <= sys.version_info[:2] <= (3,14) else 1)" >nul 2>nul
  if errorlevel 1 (
    echo Existing virtual environment uses an unsupported Python - recreating it...
    rmdir /s /q venv
  )
)

if not exist venv (
  echo Creating virtual environment with %PYCMD%...
  %PYCMD% -m venv venv
  if errorlevel 1 (
    echo Could not create the virtual environment.
    pause
    exit /b 1
  )
)
call venv\Scripts\activate

echo Checking dependencies...
python -m pip install -q --upgrade pip
pip install -q -r requirements.txt
if errorlevel 1 (
  echo.
  echo Installing the dependencies failed - see the message above.
  echo If it mentions "Microsoft Visual C++" or "Failed building wheel", use Python 3.12 or 3.13,
  echo delete the "venv" folder and run this file again.
  pause
  exit /b 1
)

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
