from langchain_groq import ChatGroq
from langchain.chains.retrieval_qa.base import RetrievalQA
from QASystem.services.vectorstore import get_vectorstore
from QASystem.config import settings


def build_rag_chain():
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatGroq(
        groq_api_key=settings.GROQ_API_KEY,
        model_name="llama3-8b-8192",
        temperature=0
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )
