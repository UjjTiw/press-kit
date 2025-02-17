from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_ORGANIZATION: str = os.getenv("OPENAI_ORGANIZATION")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")
    LANGCHAIN_TRACING_V2: bool = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"
    LANGCHAIN_ENDPOINT: str = os.getenv("LANGCHAIN_ENDPOINT")
    LANGCHAIN_API_KEY: str = os.getenv("LANGCHAIN_API_KEY")
    LANGCHAIN_PROJECT: str = os.getenv("LANGCHAIN_PROJECT")
    LANGCHAIN_RETRY_LIMIT: int = os.getenv("LANGCHAIN_RETRY_LIMIT")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY")

# Initialize settings instance
settings = Settings()
