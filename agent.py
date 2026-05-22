from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_ollama import ChatOllama
model = ChatOllama(model="llama3.1:8b")