from agents.evaluator import evaluation_chain
from agents.generator import generation_chain
from agents.searcher import agent_executor

from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough


chain = (
    RunnablePassthrough.assign(supplementary_data=agent_executor).assign(generate_message=generation_chain).assign(evaluation=evaluation_chain)
)