from crewai import Agent, Crew, Process, Task
from crewai_tools import tool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model='gpt-4o')
