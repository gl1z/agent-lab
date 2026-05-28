from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from tools import get_current_time
from prompts import SYSTEM_PROMPT

tools = [get_current_time]
model = ChatOllama(model="llama3.1:8b").bind_tools(tools)

def llm_call(state: MessagesState):
    system = SystemMessage(content=SYSTEM_PROMPT)
    return {"messages": [model.invoke([system] + state["messages"])]}

def should_continue(state: MessagesState):
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return END

graph_builder = StateGraph(MessagesState)
graph_builder.add_node("llm_call", llm_call)
graph_builder.add_node("tools", ToolNode(tools))
graph_builder.add_edge(START, "llm_call")
graph_builder.add_conditional_edges("llm_call", should_continue)
graph_builder.add_edge("tools", "llm_call")
graph = graph_builder.compile()

while True:
    user_input = input("Me: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    result = graph.invoke({"messages": [HumanMessage(content=user_input)]})
    print("Llama:", result["messages"][-1].content)