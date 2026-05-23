from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_ollama import ChatOllama
model = ChatOllama(model="llama3.1:8b")

def llm_call(state: MessagesState):
    return {"messages": [model.invoke(state["messages"])]}

def should_continue(state: MessagesState):
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return END

graph_builder = StateGraph(MessagesState)

graph_builder.add_node("llm_call", llm_call)

graph_builder.add_edge(START, "llm_call")
graph_builder.add_conditional_edges("llm_call", should_continue)

graph = graph_builder.compile()

from langchain_core.messages import HumanMessage

result = graph.invoke({"messages": [HumanMessage(content="what is 2 + 2?")]})
print(result["messages"][-1].content)