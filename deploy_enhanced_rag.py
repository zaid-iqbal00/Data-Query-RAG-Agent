import os
import subprocess
import time
import sys

def print_status(message, status="INFO"):
    symbols = {"INFO": "ℹ️", "SUCCESS": "✅", "ERROR": "❌", "WARNING": "⚠️"}
    print(f"{symbols.get(status, 'ℹ️')} {message}")

def run_command(command, description):
    print_status(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print_status(f"✓ {description} completed successfully", "SUCCESS")
            return True
        else:
            print_status(f"✗ {description} failed: {result.stderr}", "ERROR")
            return False
    except Exception as e:
        print_status(f"✗ {description} failed: {str(e)}", "ERROR")
        return False

def main():
    print("🚀 Enhanced RAG System Deployment")
    print("=" * 50)
    
    print_status("Setting up enhanced client data with financial analytics...")
    success = run_command(
        "C:/Users/syedz/OneDrive/Desktop/RAG-Agent/env/Scripts/python.exe setup_enhanced_data.py",
        "Enhanced data setup"
    )
    
    if not success:
        print_status("Data setup failed. Check MongoDB and MySQL connections.", "ERROR")
        return False
    
    time.sleep(2)
    
    print_status("Starting enhanced RAG backend server...")
    print_status("Server will run with sophisticated financial query handlers", "INFO")
    
    backend_path = "C:/Users/syedz/OneDrive/Desktop/RAG-Agent/backend/env"
    
    print(f"\n🌐 Starting server at: http://127.0.0.1:8000")
    print(f"📂 Server location: {backend_path}")
    print(f"🔧 Enhanced Analytics: 19+ sophisticated query handlers")
    
    os.chdir(backend_path)
    subprocess.run([
        "C:/Users/syedz/OneDrive/Desktop/RAG-Agent/env/Scripts/python.exe", 
        "-m", "uvicorn", "main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"
    ])

if __name__ == "__main__":
    main()
