import sys
from pathlib import Path

from shiny import App, reactive, render

# ---------------------------------------------------------
# Projekt-Root auf sys.path bringen, damit "rag" importierbar ist
# ---------------------------------------------------------
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent  # ...\semesterarbeit_app

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Jetzt können wir aus app/ und rag/ importieren
from ui import app_ui  # gleiche Ebene wie server.py
from rag.embeddings import load_vectorstore
from rag.retriever import get_retriever
from rag.qa_chain import build_qa_chain, answer_question

# ---------------------------------------------------------
# Lazy-Initialisierung der RAG-Chain
# ---------------------------------------------------------
_vectordb = None
_chain = None


def get_chain():
    """
    Lädt bei Bedarf den Vector-Store und baut die QA-Chain.
    Wird nur einmal initialisiert und danach wiederverwendet.
    """
    global _vectordb, _chain

    if _chain is None:
        print("Initialisiere RAG-Chain (lade Vector-Store)...")
        _vectordb = load_vectorstore()
        retriever = get_retriever(_vectordb)
        _chain = build_qa_chain(retriever)
        print("RAG-Chain initialisiert.")

    return _chain


def server(input, output, session):
    @reactive.Calc
    def current_answer():
        """
        Berechnet die Antwort für die aktuelle Frage.
        Wird neu berechnet, wenn der Button 'ask' geklickt wird.
        """
        input.ask()  # Reaktivität an Button-Klick binden

        question = input.question().strip()
        if not question:
            return "Bitte gib eine Frage ein.", ""

        chain = get_chain()
        full_text = answer_question(chain, question)

        # Vorerst: alles als Antwort behandeln, Quellen separat später verbessern
        answer_text = full_text
        sources_text = ""

        return answer_text, sources_text

    @output
    @render.text
    def answer():
        answer_text, _ = current_answer()
        return answer_text

    @output
    @render.text
    def sources():
        _, sources_text = current_answer()
        return (
            sources_text
            or "Quellen werden später noch besser strukturiert dargestellt."
        )


app = App(app_ui, server)
