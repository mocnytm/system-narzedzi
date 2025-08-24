import subprocess
import sys
import os
import time
from threading import Thread

class SystemManager:
    def __init__(self):
        self.server_process = None
        self.app_process = None
    
    def start_server(self):
        """Uruchamia serwer w tle"""
        venv_python = r"C:\SystemNarzedzi\venv\Scripts\python.exe"
        backend_path = r"C:\SystemNarzedzi\backend\app.py"
        
        self.server_process = subprocess.Popen(
            [venv_python, backend_path],
            creationflags=subprocess.CREATE_NO_WINDOW,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print("Serwer uruchomiony...")
    
    def start_app(self):
        """Uruchamia aplikację"""
        venv_python = r"C:\SystemNarzedzi\venv\Scripts\python.exe"
        desktop_path = r"C:\SystemNarzedzi\desktop\main.py"
        
        self.app_process = subprocess.Popen(
            [venv_python, desktop_path],
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        print("Aplikacja uruchomiona...")
    
    def monitor(self):
        """Monitoruje aplikację i zamyka wszystko gdy się zakończy"""
        if self.app_process:
            self.app_process.wait()  # Czekaj aż aplikacja się zamknie
            print("Aplikacja zamknięta, wyłączam serwer...")
            
            # Zamknij serwer
            if self.server_process:
                self.server_process.terminate()
                time.sleep(1)
                if self.server_process.poll() is None:
                    self.server_process.kill()
    
    def run(self):
        """Uruchamia cały system"""
        try:
            # Start serwera
            self.start_server()
            
            # Czekaj 3 sekundy
            time.sleep(3)
            
            # Start aplikacji
            self.start_app()
            
            # Monitoruj
            self.monitor()
            
        except Exception as e:
            print(f"Błąd: {e}")
        finally:
            # Upewnij się że wszystko jest zamknięte
            if self.server_process:
                self.server_process.terminate()
            if self.app_process:
                self.app_process.terminate()

if __name__ == "__main__":
    manager = SystemManager()
    manager.run()