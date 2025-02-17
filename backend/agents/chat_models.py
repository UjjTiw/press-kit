# Load and interact with LLM
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from .config import settings

gpt4o = ChatOpenAI(
    model="gpt-4o",
    api_key=SecretStr(settings.OPENAI_API_KEY),
    temperature=0,
    max_tokens=8192,
    timeout=60,
)

gpt4o_mini = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=SecretStr(settings.OPENAI_API_KEY),
    temperature=0,
    max_tokens=8192,
    timeout=60,
)

o1_mini = ChatOpenAI(
    model="o1-mini",
    api_key=SecretStr(settings.OPENAI_API_KEY),
    temperature=1,
    timeout=60,
)
