 Multi-Agent Content Generation System

## Problem Statement
Design a system that automatically generates structured content pages from a given product dataset using a true multi-agent architecture. The system must be modular, extensible, and produce machine-readable outputs without relying on hard-coded logic.

---

## Solution Overview
This project implements a lightweight agentic automation system where independent agents collaborate through an orchestrator. Each agent has a single responsibility and operates on shared state, allowing dynamic coordination instead of static function calls.

The system generates:
- FAQ Page
- Product Description Page
- Comparison Page (with a fictional product)

All outputs are produced as structured JSON.

---

## Scope & Assumptions
- Only the provided product data is used
- No external research or enrichment is performed
- Product B in comparison is fictional and statically defined
- Focus is on system design, not content creativity

---

## System Design (Core)
The system follows a **state-driven agent orchestration model**.

### Agents
- **ProductParserAgent**  
  Normalizes raw input data into an internal product model.

- **QuestionGenerationAgent**  
  Generates categorized user questions from product data.

- **FAQAgent**  
  Builds FAQ content using product data and generated questions.

- **ProductPageAgent**  
  Generates structured product page content.

- **ComparisonAgent**  
  Compares the main product with a fictional Product B.

Each agent:
- Is stateless
- Has a single responsibility
- Exposes a `run()` interface

---

### Orchestration Flow
The orchestrator controls execution by passing a shared state object across agents.

Raw Input
↓
ProductParserAgent
↓
QuestionGenerationAgent
↓
FAQAgent / ProductPageAgent / ComparisonAgent
↓
JSON Outputs



This design allows agents to be added, removed, or reordered without modifying other agents.

---

## Extensibility
- New page types can be added by introducing new agents
- Logic can be extended without refactoring orchestration
- LLM-backed agents can replace rule-based agents in future

---

## Output Structure
Each page is generated as clean, machine-readable JSON and can be consumed by downstream systems such as CMS pipelines or search indexes.

---

## Conclusion
This project demonstrates a true agentic architecture with clear agent autonomy, dynamic orchestration, and production-oriented design principles aligned with the assignment requirements