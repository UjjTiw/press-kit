from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain.agents import AgentExecutor, create_openai_functions_agent
from ..chat_models import gpt4o
from langchain.prompts import ChatPromptTemplate
from ..config import settings
from .base import base_message

api_wrapper = TavilySearchAPIWrapper(tavily_api_key=settings.TAVILY_API_KEY)
tavily_tool = TavilySearchResults(api_wrapper=api_wrapper)


tools = [tavily_tool]

prompt = ChatPromptTemplate.from_messages(base_message)

# Create an AI agent with the specified LLM and tools, and the customized prompt
agent = create_openai_functions_agent(gpt4o, tools, prompt)

# Set up an executor for the agent, specifying the agent, tools, and enabling verbose output
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)