@echo off
title Open RAG Agent Interface
color 0B

REM Check if HTML file exists
if not exist "simple-frontend.html" (
    echo Error: simple-frontend.html not found!
    echo Make sure you're running this from the RAG-Agent directory.
    pause
    exit /b 1
)

REM Open the web interface in default browser
echo Opening web interface...
start "" "simple-frontend.html"

REM Wait 3 seconds
timeout /t 3 /nobreak > nul

REM Check if server is running before opening API docs
echo Checking if server is running...
powershell -Command "try { Invoke-WebRequest -Uri 'http://127.0.0.1:8000/health' -TimeoutSec 2 -UseBasicParsing | Out-Null; exit 0 } catch { exit 1 }"

if %errorlevel% equ 0 (
    echo Server is running. Opening API documentation...
    start "" "http://127.0.0.1:8000/docs"
) else (
    echo Warning: Server is not running at http://127.0.0.1:8000
    echo Start the server first using start.bat or quick_start.bat
)

echo.
echo RAG Agent interfaces opened successfully!
echo.
echo Web Interface: simple-frontend.html
echo API Docs: http://127.0.0.1:8000/docs (if server is running)
echo.
echo Press any key to exit...
pause > nul
