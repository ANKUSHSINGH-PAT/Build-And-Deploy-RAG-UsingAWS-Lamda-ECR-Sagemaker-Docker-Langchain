from langchain_community.vectorstores import Chroma
from QASystem.config import settings
from QASystem.services.embedding import get_embedding_model


def get_vectorstore():
    embedding = get_embedding_model()

    return Chroma(
        persist_directory=settings.VECTOR_DB_DIR,
        embedding_function=embedding
    )
