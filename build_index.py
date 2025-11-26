from rag.loaders import load_all_documents
from rag.splitter import split_documents
from rag.embeddings import build_vectorstore


def main():
    print("Lade Dokumente ...")
    docs = load_all_documents()
    print(f"{len(docs)} Dokument(e) geladen.")

    print("Erzeuge Chunks ...")
    chunks = split_documents(docs)
    print(f"{len(chunks)} Chunks erzeugt.")

    print("Baue Vector-Store (Chroma) ...")
    build_vectorstore(chunks)

    print("Fertig. Index ist unter 'data/index' gespeichert.")


if __name__ == "__main__":
    main()
