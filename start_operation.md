# START OPERATION - RAG Agent Project

## 🚀 Complete Project Startup Guide

### Prerequisites Check
Before starting, ensure you have:
- MongoDB running on localhost:27017
- MySQL server running with database "your_mysql_db"
- Python virtual environment created
- All dependencies installed

---

## 📋 Step-by-Step Startup Process

### 1. Navigate to Project Directory
```powershell
cd C:\Users\syedz\OneDrive\Desktop\RAG-Agent
```

### 2. Activate Python Virtual Environment
```powershell
env\Scripts\activate
```

### 3. Verify Dependencies (Optional - if fresh install)
```powershell
env\Scripts\python.exe -m pip install pymongo mysql-connector-python fastapi uvicorn transformers torch langchain langchain-huggingface langchain-community
```

### 4. Setup Enhanced Database (First time only or data refresh)
```powershell
env\Scripts\python.exe setup_enhanced_data.py
```

### 5. Start the Backend Server
```powershell
cd backend\env
..\..\env\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 6. Open Frontend Interface
- Open `simple-frontend.html` in your web browser
- Or visit `http://127.0.0.1:8000/docs` for API documentation

---

## 🔧 Alternative Quick Start Methods

### Method 1: Using Deploy Script
```powershell
env\Scripts\python.exe deploy_enhanced_rag.py
```

### Method 2: Manual Terminal Commands
```powershell
# Terminal 1 - Backend
cd C:\Users\syedz\OneDrive\Desktop\RAG-Agent\backend\env
C:\Users\syedz\OneDrive\Desktop\RAG-Agent\env\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Terminal 2 - Testing (Optional)
cd C:\Users\syedz\OneDrive\Desktop\RAG-Agent
env\Scripts\python.exe test_enhanced_queries.py
```

---

## ✅ Verification Steps

### 1. Check Server Status
Visit: `http://127.0.0.1:8000/health`
Expected response: `{"status": "ok"}`

### 2. Test Basic Endpoints
- `http://127.0.0.1:8000/profiles` - Client profiles
- `http://127.0.0.1:8000/transactions` - Transaction data
- `http://127.0.0.1:8000/relationship_managers` - Manager data

### 3. Test Enhanced Queries in Frontend
Try these sample queries:
- "Which sectors are our clients most heavily invested in?"
- "What's the diversification score for each client's portfolio?"
- "Show me clients who might be interested in ESG investments"

---

## 🚨 Troubleshooting Common Issues

### Issue: MongoDB Connection Error
**Solution:**
```powershell
# Start MongoDB service
net start MongoDB
# Or manually start MongoDB from installation directory
```

### Issue: MySQL Connection Error
**Solution:**
```powershell
# Check MySQL service
net start MySQL80
# Verify credentials in main.py (user: root, password: your_mysql_password_here)
```

### Issue: Port 8000 Already in Use
**Solution:**
```powershell
# Kill existing processes on port 8000
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F
```

### Issue: Python Dependencies Missing
**Solution:**
```powershell
cd C:\Users\syedz\OneDrive\Desktop\RAG-Agent
env\Scripts\python.exe -m pip install --upgrade pip
env\Scripts\python.exe -m pip install -r requirements.txt
```

### Issue: Virtual Environment Not Found
**Solution:**
```powershell
# Recreate virtual environment
python -m venv env
env\Scripts\activate
env\Scripts\python.exe -m pip install pymongo mysql-connector-python fastapi uvicorn transformers torch langchain langchain-huggingface langchain-community
```

---

## 📁 Project Structure Overview
```
RAG-Agent/
├── env/                         # Python virtual environment
├── backend/env/main.py          # Main backend server
├── setup_enhanced_data.py       # Database setup script
├── simple-frontend.html         # Frontend interface
├── test_enhanced_queries.py     # Testing script
├── deploy_enhanced_rag.py       # Automated deployment
└── start_operation.md           # This startup guide
```

---

## 🎯 Success Indicators

When everything is working correctly, you should see:

### Backend Terminal Output:
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Frontend Working:
- HTML interface loads without errors
- Chat interface responds to messages
- Quick data access buttons work
- System health shows "✅ Healthy"

### Advanced Analytics Working:
- Complex financial queries return detailed responses
- Sector analysis provides percentage breakdowns
- Client risk assessments show detailed scoring
- Performance metrics include calculated analytics

---

## 🚀 You're Ready!

Once all steps are complete, your enhanced RAG system with 19+ sophisticated financial analytics capabilities is fully operational and ready for complex business intelligence queries.
