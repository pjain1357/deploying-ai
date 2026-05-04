from langgraph.graph import StateGraph, MessagesState, START
from langchain.chat_models import init_chat_model
from langgraph.prebuilt.tool_node import ToolNode, tools_condition
from langchain_core.messages import SystemMessage,  HumanMessage

from dotenv import load_dotenv
import json
import os

from .prompts import return_instructions
from .service_functionCall import convert_currency
from .service_api import get_metropolitan_museum_facts, get_art_institute_facts
from utils.logger import get_logger


_logs = get_logger(__name__)
load_dotenv(".env")
load_dotenv(".secrets")

os.environ["LANGCHAIN_TRACING_V2"] = "false"

chat_agent = init_chat_model(
    "openai:gpt-4o-mini",
    base_url='https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1', 
    api_key='any value',
    default_headers={"x-api-key": os.getenv('API_GATEWAY_KEY')}
)


tools = [ convert_currency, get_metropolitan_museum_facts, get_art_institute_facts ]

instructions = return_instructions()



# @traceable(run_type="llm")
def call_model(state: MessagesState):
    """LLM decides whether to call a tool or not"""
    response = chat_agent.bind_tools(tools).invoke( [SystemMessage(content=instructions)] + state["messages"])

    """ if "convert" in response.content:
        # Extract the arguments from the response
        try:
            args = json.loads(response.content.split("convert_currency(")[1].split(")")[0])
            amount = args["amount"]
            from_currency = args["from_currency"]
            to_currency = args["to_currency"]
            
            # Call the convert_currency function with the extracted arguments
            conversion_result = convert_currency(amount, from_currency, to_currency)
            
            # Return the result as a new message that gets added to the state
            return {
                "messages": [HumanMessage(content=conversion_result)]
            }
        except Exception as e:
            _logs.error(f"Error parsing convert_currency arguments: {e}")
            return {
                "messages": [HumanMessage(content="Sorry, I couldn't parse the currency conversion request.")]
            } """
    return {
        "messages": [response]
    }

def get_graph():
    
    builder = StateGraph(MessagesState)
    builder.add_node(call_model)
    builder.add_node(ToolNode(tools))
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges(
        "call_model",
        tools_condition,
    )
    builder.add_edge("tools", "call_model")
    graph = builder.compile()
    return graph

