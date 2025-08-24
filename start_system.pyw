import subprocess
import time
import os
import sys

def start_system():
    """Uruchamia system w tle"""
    # Ścieżki
    venv_python = r"C:\SystemNarzedzi\venv\Scripts\pythonw.exe"
    backend_path = r"C:\SystemNarzedzi\backend\app.py"
    desktop_path = r"C:\SystemNarzedzi\desktop\main.py"
    
    try:
        # Uruchom serwer
        subprocess.Popen([venv_python, backend_path], 
                        creationflags=subprocess.CREATE_NO_WINDOW)
        
        # Poczekaj 3 sekundy
        time.sleep(3)
        
        # Uruchom aplikację
        subprocess.Popen([venv_python, desktop_path],
                        creationflags=subprocess.CREATE_NO_WINDOW)
        
        print("System uruchomiony!")
        
    except Exception as e:
        input(f"Błąd: {e}\nNaciśnij Enter...")

if __name__ == "__main__":
    start_system()