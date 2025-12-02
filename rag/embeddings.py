from typing import List

from langchain_core.documents import Document
from langchain_chroma import Chroma

from .config import INDEX_DIR, get_openai_embeddings


def build_vectorstore(chunks: List[Document]) -> Chroma:
    """
    Baut einen neuen Chroma-Vector-Store aus Chunks und speichert ihn persistent.
    """
    embeddings = get_openai_embeddings()
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(INDEX_DIR),
    )
    vectordb.persist()
    return vectordb


def load_vectorstore() -> Chroma:
    """
    Lädt einen bestehenden Chroma-Vector-Store.
    """
    embeddings = get_openai_embeddings()
    return Chroma(
        embedding_function=embeddings,
        persist_directory=str(INDEX_DIR),
    )
