@echo off
title Complete RAG Agent Setup
color 0E

echo.
echo =============================================
echo   🚀 Complete RAG Agent Setup & Launch 🚀
echo =============================================
echo.

REM Navigate to project directory
echo Step 1: Navigating to project directory...
cd /d "C:\Users\syedz\OneDrive\Desktop\RAG-Agent"
if %errorlevel% neq 0 (
    echo ❌ Error: Could not find project directory
    pause
    exit /b 1
)

REM Activate virtual environment
echo Step 2: Activating virtual environment...
call env\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ❌ Error: Could not activate virtual environment
    pause
    exit /b 1
)

REM Setup database
echo Step 3: Setting up enhanced database...
python setup_enhanced_data.py
if %errorlevel% neq 0 (
    echo ❌ Error: Database setup failed
    pause
    exit /b 1
)

REM Navigate to backend directory
echo Step 4: Navigating to backend...
cd backend\env
if %errorlevel% neq 0 (
    echo ❌ Error: Could not find backend directory
    pause
    exit /b 1
)

REM Open web interface
echo Step 5: Opening web interface...
start "" "C:\Users\syedz\OneDrive\Desktop\RAG-Agent\simple-frontend.html"

REM Wait a moment
timeout /t 2 /nobreak > nul

echo.
echo ✅ Setup complete! Starting server...
echo.
echo 🎯 Your RAG Agent is ready for celebrity wealth queries!
echo 🌐 Web interface should open automatically
echo 📚 API docs will be available at: http://127.0.0.1:8000/docs
echo.

REM Set Python path and start server
set PYTHONPATH=C:\Users\syedz\OneDrive\Desktop\RAG-Agent\backend\env
C:\Users\syedz\OneDrive\Desktop\RAG-Agent\env\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

echo.
echo ❌ Server stopped. Press any key to exit...
pause > nul
