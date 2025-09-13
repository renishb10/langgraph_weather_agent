from langchain_core.tools import tool
from langchain_tavily import TavilySearch

@tool
def triple(num: float) -> float:
    """
    param num: a number to triple and
    returns: the triple of the input number
    """
    return float(num) * 3

tools = [TavilySearch(max_result=1), triple]