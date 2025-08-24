========================================
    SYSTEM ZARZĄDZANIA NARZĘDZIAMI
         Instrukcja Obsługi
========================================

📌 URUCHAMIANIE SYSTEMU:
------------------------
1. Kliknij dwukrotnie na START.bat
2. Poczekaj aż uruchomi się serwer i aplikacja
3. Zaloguj się: admin / admin123

📌 GŁÓWNE FUNKCJE:
-----------------
✅ Dodawanie narzędzi
   - Kliknij "➕ Dodaj narzędzie"
   - Wypełnij formularz
   - System automatycznie generuje unikalny kod

✅ Wypożyczanie
   - Kliknij "Wypożycz" przy dostępnym narzędziu
   - Wybierz projekt
   - Dodaj notatkę

✅ Zwrot
   - Kliknij "Zwróć" przy wypożyczonym narzędziu
   - Opisz stan narzędzia

✅ Historia
   - Kliknij "📋 Historia" aby zobaczyć kto wypożyczał

✅ Kody QR
   - Kliknij "📱 QR" aby wygenerować kod
   - Wydrukuj i przyklej na narzędzie

✅ Eksport do Excel
   - Kliknij "📥 Eksport Excel"
   - Wybierz miejsce zapisu
   - Plik zawiera wszystkie dane

✅ Statystyki
   - Kliknij "📊 Statystyki"
   - Zobacz podsumowanie systemu

📌 FILTRY I WYSZUKIWANIE:
------------------------
- Wpisz tekst w pole "Szukaj"
- Wybierz status z listy rozwijanej
- Kliknij nagłówek kolumny aby sortować

📌 KOPIA ZAPASOWA:
-----------------
- Uruchom BACKUP.bat regularnie
- Kopie zapisują się w folderze backup

📌 ROZWIĄZYWANIE PROBLEMÓW:
--------------------------
❓ Aplikacja nie startuje?
   → Sprawdź czy serwer działa (okno CMD)
   
❓ "Nie można połączyć z serwerem"?
   → Uruchom ponownie START.bat
   
❓ Zgubione hasło?
   → Domyślne: admin / admin123

📌 STRUKTURA FOLDERÓW:
---------------------
SystemNarzedzi\
├── backend\        (serwer + baza danych)
├── desktop\        (aplikacja)
├── backup\         (kopie zapasowe)
├── venv\           (środowisko Python)
├── START.bat       (uruchomienie)
└── BACKUP.bat      (kopia zapasowa)

========================================
Wersja: 1.0
Data: Sierpień 2024
Autor: System stworzony z pomocą AI
========================================