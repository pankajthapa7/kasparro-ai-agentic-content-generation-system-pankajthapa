Kasparro – Agentic Content Generation System
Overview

This project implements a true multi-agent content generation system that converts structured product data into multiple machine-readable content pages using autonomous, modular agents coordinated through an orchestration mechanism.

The focus of this system is agentic design, not content writing or prompting.

What This System Does

Given a single product input, the system autonomously generates:

FAQ Page (faq.json)

Product Description Page (product_page.json)

Comparison Page (comparison_page.json)

All outputs are:

Deterministic

Template-driven

Fully machine-readable JSON

Agentic Architecture (High Level)

Each agent has one responsibility and no hidden state.

Raw Product Data
        |
        v
+-------------------+
| Product Parser    |
+-------------------+
        |
        v
+-------------------+
| Question Generator|
+-------------------+
        |
        v
+-------------------+
| Content Logic     |
+-------------------+
        |
        v
+-------------------+
| Page Agents       |
| (FAQ / Product / |
|  Comparison)      |
+-------------------+
        |
        v
+-------------------+
| Orchestrator      |
+-------------------+
        |
        v
JSON Outputs

Key Design Principles

True Agent Autonomy
Each agent operates independently and is invoked by the orchestrator via explicit inputs and outputs.

No Monolithic Flow
Logic, templates, and orchestration are clearly separated.

Composable & Extensible
New agents or page types can be added without modifying existing agents.

Deterministic Execution
No hard-coded page logic or static content assembly.


main.py

How to Run the System
1. Run the pipeline
python main.py

2. Generated Outputs

The system will generate:

output/
 ├── faq.json
 ├── product_page.json
 └── comparison_page.json


Each file is produced via agent coordination, not manual wiring.
