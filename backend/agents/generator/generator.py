from ..chat_models import gpt4o
from .base import generation_messages
from typing import Any

from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import OutputFixingParser
from langchain.output_parsers.prompts import NAIVE_FIX_PROMPT
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSerializable

from ..config import settings

def build_output_fixing_parser(
    *, parser: Any, llm: Any = gpt4o
) -> OutputFixingParser[Any]:
    """Build output fixing parser with retry capability"""
    retry_chain: RunnableSerializable[dict[str, Any], str] = NAIVE_FIX_PROMPT | llm | StrOutputParser()
    return OutputFixingParser(
        parser=parser,
        retry_chain=retry_chain,
        max_retries=settings.LANGCHAIN_RETRY_LIMIT,
    )


parser = build_output_fixing_parser(parser=StrOutputParser(), llm=gpt4o)

generation_prompt = ChatPromptTemplate.from_messages(generation_messages)
generation_chain = (
    generation_prompt
    | gpt4o
    | parser
)