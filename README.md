# agent-lab

A LangGraph agent running locally on Ollama. This is the test subject for 
Apodex — my dissertation project on runtime security monitoring for LLM agents.

## What this is

A minimal LangGraph agent built to study how LLM agents misbehave. No 
guardrails, no safety layer. The point is to observe attack patterns cleanly 
before building detectors for them in Apodex.

## Why this exists

Apodex needs something to monitor. This is it. Every finding here maps to 
a detector I'm building.

## Stack

- LangGraph
- Ollama (Llama 3.1 8B) — running locally on a 3080 Ti
- Python 3.13
- Tools: get_current_time, read_notes_file
- Memory: conversation history persists within a session
- Tracing: OpenTelemetry + Arize Phoenix

## How to run

Start Phoenix first — it needs to be running before the agent so it can 
receive traces:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install langgraph langchain langchain-community langchain-ollama opentelemetry-sdk openinference-instrumentation-langchain opentelemetry-exporter-otlp-proto-grpc arize-phoenix
python -m phoenix.server.main serve
```

Then in a second terminal:

```bash
.venv\Scripts\activate
python agent.py
```

Traces show up at `http://localhost:6006`.

## What's been tested

28 tests in `logs/sample_runs.md` across five categories:

- Prompt injection and jailbreaking
- Tool hallucination and misuse
- Insecure output
- Excessive agency
- Data exfiltration

## Known gap

If the model reproduces sensitive data from conversation history rather than 
calling a tool again, no span is generated and Apodex misses it. Output 
scanning on the final LLM response span is the fix — not just tool result 
scanning.

## Apodex

[github.com/gl1z/apodex](https://github.com/gl1z/apodex)