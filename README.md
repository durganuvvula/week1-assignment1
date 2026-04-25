Agentic AI Enterprise Mastery Bootcamp · Day 1
This project demonstrates why naive string-based LLM calls lose context across turns, and how the LangChain Messages API fixes the problem with structured SystemMessage / HumanMessage objects.

The goal is not to print outputs — it is to understand system behavior in production.

What the Script Demonstrates
Part 1 — Naïve string-based invocation. Two independent llm.invoke("...") calls. Each call is stateless, so the second question's reference to "this system" has no antecedent. The model is forced to guess, leading to inconsistent or generic answers.
Part 2 — Messages API fix. A list of SystemMessage and HumanMessage objects is passed to llm.invoke(messages). The full conversation is reconstructed on every call, so "this system" unambiguously resolves to the medical insurance claims AI established earlier.
A reflection block at the bottom of app.py discusses why this matters in production AI systems.
