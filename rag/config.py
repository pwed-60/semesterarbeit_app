
from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

# Projektwurzel (…/semesterarbeit_app)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Wissensordner (Default aus .env oder fixer Pfad)
KNOWLEDGE_DIR = Path(
    os.getenv(
        "KNOWLEDGE_DIR",
        r"C:\Users\weder\OneDrive\Dokumente\02_wb\25-10 CAS Generative KI\semesterarbeit\Wissensordner",
    )
)

# Ordner für den persistenten Vector Store
INDEX_DIR = PROJECT_ROOT / "data" / "index"
INDEX_DIR.mkdir(parents=True, exist_ok=True)

# OpenAI Konfiguration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")  # optional
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
OPENAI_EMBED_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")

# Chunking-Konfiguration
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "800"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))


def get_openai_llm():
    """
    Erzeugt ein LangChain-Chat-LLM für OpenAI.
    """
    from langchain_openai import ChatOpenAI

    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY ist nicht gesetzt (.env prüfen).")

    return ChatOpenAI(
        model=OPENAI_MODEL,
        temperature=0.1,
        openai_api_key=OPENAI_API_KEY,
        openai_api_base=OPENAI_BASE_URL or None,
    )


def get_openai_embeddings():
    """
    Erzeugt ein Embedding-Objekt für OpenAI.
    """
    from langchain_openai import OpenAIEmbeddings

    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY ist nicht gesetzt (.env prüfen).")

    return OpenAIEmbeddings(
        model=OPENAI_EMBED_MODEL,
        openai_api_key=OPENAI_API_KEY,
        openai_api_base=OPENAI_BASE_URL or None,
    )
