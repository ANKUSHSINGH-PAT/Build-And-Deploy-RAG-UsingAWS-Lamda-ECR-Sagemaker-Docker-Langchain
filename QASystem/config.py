from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

class Settings(BaseSettings):
    APP_NAME: str = "LLM Q&A System"
    GROQ_API_KEY: str
    VECTOR_DB_DIR: str = "./vector_db"

    class Config:
        env_file = ".env"


settings = Settings()
