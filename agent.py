from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage

model = ChatOllama(model="llama3.1:8b")

def llm_call(state: MessagesState):
    system = SystemMessage(content="You are a helpful assistant. Be concise.")
    return {"messages": [model.invoke([system] + state["messages"])]}

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

while True:
    user_input = input("Me: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    result = graph.invoke({"messages": [HumanMessage(content=user_input)]})
    print("Llama:", result["messages"][-1].content)