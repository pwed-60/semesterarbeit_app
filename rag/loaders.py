from pathlib import Path
from typing import List

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
)
from langchain_core.documents import Document  # <- neu

from .config import KNOWLEDGE_DIR

SUPPORTED_SUFFIXES = {".pdf", ".docx", ".txt"}


def iter_files(base_dir: Path):
    """
    Iterator über alle unterstützten Dateien im Wissensordner.
    """
    for path in base_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES:
            yield path


def load_single_file(path: Path) -> List[Document]:
    """
    Lädt ein einzelnes Dokument als Liste von LangChain-Documents.
    """
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        loader = PyPDFLoader(str(path))
    elif suffix == ".docx":
        loader = Docx2txtLoader(str(path))
    elif suffix == ".txt":
        loader = TextLoader(str(path), encoding="utf-8")
    else:
        return []

    docs = loader.load()
    for d in docs:
        d.metadata.setdefault("source", str(path))
    return docs


def load_all_documents() -> List[Document]:
    """
    Lädt alle Dokumente aus dem Wissensordner.
    """
    all_docs: List[Document] = []
    if not KNOWLEDGE_DIR.exists():
        raise FileNotFoundError(f"Wissensordner existiert nicht: {KNOWLEDGE_DIR}")

    for file_path in iter_files(KNOWLEDGE_DIR):
        all_docs.extend(load_single_file(file_path))

    return all_docs
