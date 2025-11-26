from typing import Any

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from .config import get_openai_llm

SYSTEM_PROMPT = """Du bist ein hilfreicher Assistent und beantwortest Fragen **nur** anhand des bereitgestellten Kontexts.
Wenn die Information nicht im Kontext enthalten ist, sag klar, dass du es nicht weisst.
Antworte auf Deutsch (Schweiz).
Führe am Ende deiner Antwort immer die verwendeten Quellen auf.
"""


def _format_docs(docs) -> str:
    """
    Formatiert Dokumente für den Prompt.
    """
    formatted = []
    for i, d in enumerate(docs):
        src = d.metadata.get("source", "")
        formatted.append(f"[{i+1}] {d.page_content}\n(Quelle: {src})")
    return "\n\n".join(formatted)


def build_qa_chain(retriever: Any):
    """
    Baut eine einfache RAG-Chain (Retriever -> Prompt -> LLM -> Text).
    """
    llm = get_openai_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", "Frage:\n{question}\n\nKontext:\n{context}"),
        ]
    )

    chain = (
        {
            "context": retriever | _format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


def answer_question(chain, question: str) -> str:
    """
    Führt die Chain aus und gibt die Antwort zurück.
    """
    return chain.invoke(question)
