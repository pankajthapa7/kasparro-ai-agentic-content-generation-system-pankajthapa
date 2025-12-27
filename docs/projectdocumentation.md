# Applied AI Engineer Challenge – Multi-Agent Content Generation System

## Problem Statement
The goal of this assignment is to design a modular agent-based system that takes structured product data as input and automatically generates machine-readable content pages such as FAQs, product descriptions, and product comparisons.

The focus of the task is on system design, agent orchestration, and reusable logic rather than content creativity or domain knowledge.

---

## Solution Overview
This project implements a simple multi-agent pipeline where each agent has a clear and single responsibility. The system parses product data, generates structured questions, applies reusable content logic, and assembles multiple content pages using templates.

All outputs are generated as clean JSON files and the entire flow is controlled by an orchestrator.

---

## Scope & Assumptions
- Only the provided product data is used.
- No external data or research is added.
- Product B in the comparison page is fictional but statically defined.
- The system is rule-based and deterministic.
- The focus is on backend automation, not UI or frontend rendering.

---

## System Design
The system is designed using independent agents with clear input and output boundaries.
This project is designed as a modular, agent-based automation system that converts structured product data into multiple machine-readable content pages.
The focus of the design is clear separation of responsibilities, reusability, and extensibility.

High-Level Flow

The system follows a step-by-step pipeline:

Raw Product Data
→ Product Parser Agent
→ Question Generation Agent
→ Content Logic Agent
→ Template Engine
→ Page Assembly Agent
→ JSON Outputs

Each step is handled by a dedicated agent with a single responsibility.



### Main Components
- **ProductParserAgent**  
  Converts raw product input into a normalized internal product model.

- **QuestionGenerationAgent**  
  Generates categorized user questions using predefined rules.

- **ContentLogicAgent**  
  Contains reusable logic blocks for benefits, usage, ingredients, and safety information.

- **Template Engine**  
  Defines the structure of FAQ, Product, and Comparison pages and pulls required logic blocks.

- **ComparisonLogicAgent**  
  Handles rule-based comparison between the main product and a fictional Product B.

- **PageAssemblyAgent**  
  Assembles final page outputs in JSON format.

- **Orchestrator**  
  Controls the execution flow between agents and ensures the full pipeline runs in sequence.

---

## Output
The system generates the following JSON files:
- `faq.json`
- `product_page.json`
- `comparison_page.json`

Each file is fully machine-readable and follows a consistent schema.

---

## Conclusion
This system demonstrates a production-style agentic architecture with clear separation of concerns, reusable logic, and extensible design. New products or page types can be added with minimal changes to the existing pipeline.
