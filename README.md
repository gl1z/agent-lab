# agent-lab

A LangGraph agent running locally via Ollama. Built as the test subject 
for Apodex, a runtime security monitoring framework for LLM agents.

## What this is

This repo contains a simple LangGraph agent used to study and document 
unsafe behaviour in LLM agents before building detectors for it. The 
agent is intentionally minimal; no guardrails, no safety layer, so 
that attack patterns can be observed cleanly.

## Why this exists

Apodex needs a real agent to monitor. This is that agent. Every 
vulnerability documented here maps to a detector in Apodex.

## Stack
- LangGraph
- Ollama (Llama 3.1 8B)
- Python 3.13
- Tools: get_current_time

## How to run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install langgraph langchain langchain-community langchain-ollama
python agent.py
```

## Current agent behaviour

24 security behaviour tests documented in `logs/sample_runs.md` covering:
- Prompt injection and jailbreaking
- Tool hallucination and misuse
- Insecure output generation
- Excessive agency
- Data exfiltration attempts

## Test prompts

Categorised attack prompts in `test_prompts/` — one file per detector category.

## Link to Apodex

This agent is the test subject for [Apodex](https://github.com/gl1z/apodex) 
— a dissertation project exploring runtime security monitoring for LangGraph 
agents using OpenTelemetry.