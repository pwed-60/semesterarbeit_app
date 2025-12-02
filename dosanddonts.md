## Do’s & Don’ts: `.env` und Secrets in Git-Repos

### Do’s

- **`.env` ignorieren**
  - `.env` immer in `.gitignore` eintragen:
    ```gitignore
    .env
    ```
  - Überprüfen:
    ```bash
    git ls-files .env   # sollte keine Ausgabe liefern
    ```

- **Konfiguration über Umgebungsvariablen**
  - API-Keys, Verbindungs-Strings usw. nur über `.env` / Environment-Variablen holen, z. B.:
    ```python
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ```

- **Beispiel-Config verwenden**
  - Eine öffentliche Vorlage verwenden:
    - `.env.example` mit Platzhaltern (ohne echte Secrets)
    - Im README erklären, welche Werte gesetzt werden müssen.

- **Bei Leaks: sofort reagieren**
  - Schlüssel im jeweiligen Dienst (z. B. OpenAI) **rotieren**:
    - alten Key deaktivieren,
    - neuen Key generieren und lokal in `.env` eintragen.
  - In GitHub bei Secret-Scanning:
    - „I have revoked this secret“ bestätigen,
    - Push explizit erlauben.

---

### Don’ts

- **Nie echte Secrets committen**
  - Keine API-Keys, Passwörter oder Tokens in:
    - `.py`-Dateien,
    - `.env`,
    - Notizen im Repo (z. B. `notes.txt`).

- **Keine hart codierten Keys**
  - Niemals so:
    ```python
    OPENAI_API_KEY = "sk-123456789..."
    ```

- **Keine Logs mit sensiblen Daten versionieren**
  - Logfiles, Dumps, Index-/Cache-Dateien nicht commiten:
    - in `.gitignore` eintragen (z. B. `data/index/`, `*.log`).

---

### Praktische Checks

- Vor erstem Push:
  ```bash
  git ls-files | xargs grep -ni "sk-" 2>nul
