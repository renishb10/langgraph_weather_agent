from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tools import tools

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)
