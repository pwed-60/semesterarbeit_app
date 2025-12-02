# Semesterarbeit – Dokumenten-Chatbot (Shiny + LangChain + OpenAI)

Dieses Projekt ist eine kleine RAG-basierte Web-App:
- UI: Shiny for Python (läuft im Browser)
- RAG: LangChain (Dokumenten-Loader, Chunking, Embeddings, Vector Store, Retrieval)
- LLM: OpenAI API

## Setup

1. Repository-Ordner anlegen

   ```powershell
   cd C:\Dev
   mkdir semesterarbeit_app
   cd .\semesterarbeit_app




## Anwendung starten

### Voraussetzungen

- Python 3.11 (oder kompatible Version) ist installiert
- Dieses Repository ist lokal geklont (z. B. unter `C:\Dev\semesterarbeit_app`)
- Virtuelle Umgebung und Abhängigkeiten sind eingerichtet (siehe Abschnitt „Setup“)

### Setup (einmalig)

Falls noch nicht geschehen, führe einmalig folgende Schritte aus:

1. Terminal oder PowerShell öffnen.Scripts\Activate.ps1
Abhängigkeiten
2. In das Projektverzeichnis wechseln:

   ```powershell
   cd C:\Dev\semesterarbeit_app

3. Virtuelle Umgebung erstellen (falls .venv noch nicht existiert):
   python -m venv .venv

4. Virtuelle Umgebung aktivieren:
   .\.venv\Scripts\Activate.ps1

5. Abhängigkeiten installieren:
   pip install -r requirements.txt


1. VS Code öffnen

2. VS Code starten.

   Menü: Datei → Ordner öffnen…

   Ordner C:\Dev\semesterarbeit_app auswählen und vertrauen.

3. Python-Interpreter aus .venv wählen

   Ctrl + Shift + P → „Python: Interpreter auswählen“.

   Interpreter wählen, der zu .venv gehört (z. B. Python 3.x ('.venv': venv)).

4. Terminal in VS Code öffnen

   Menü: Terminal → Neues Terminal.

   Sicherstellen, dass das Terminal im Projektordner ist:
      PS C:\Dev\semesterarbeit_app>.

4. Virtuelle Umgebung aktivieren (falls nicht automatisch)

      Wenn im Prompt noch kein (.venv) steht:

         .\.venv\Scripts\Activate.ps1


5. Shiny-App starten

   Im aktivierten Environment:

      shiny run --reload app/server.py


   Im Terminal erscheint eine Meldung wie:

      INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)


6. App im Browser öffnen

      Die angezeigte URL (z. B. http://127.0.0.1:8000) im Browser öffnen
      oder im VS-Code-Terminal mit Ctrl + Klick öffnen.

7. Server stoppen

   Im Terminal-Fenster mit der laufenden App Ctrl + C drücken.