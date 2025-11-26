from langchain_community.vectorstores import Chroma


def get_retriever(vectordb: Chroma, k: int = 4):
    """
    Erzeugt einen Retriever aus dem Vector-Store.
    """
    return vectordb.as_retriever(search_kwargs={"k": k})
