Kasparro – Agentic Content Generation System
Overview

This project implements a modular, agent-based automation system that converts structured product data into multiple machine-readable content pages (FAQ, Product, Comparison).

The focus is system design and agent orchestration, not content creativity or UI.

@Key Design Principles

Multi-agent architecture with single-responsibility agents

Deterministic, rule-based logic (no external data or prompts)

Reusable content logic blocks

Template-driven page generation

Central orchestration pipeline

@High-Level System Flow
Raw Product Data
        ↓
Product Parser Agent
        ↓
Normalized Product Model
        ↓
Question Generation Agent
        ↓
Reusable Content Logic Blocks
        ↓
Template Engine
        ↓
Page Assembly Agent
        ↓
JSON Outputs

@Agent Responsibilities (At a Glance)
Agent	Responsibility
ProductParserAgent	Normalize raw product input
QuestionGenerationAgent	Generate categorized user questions
ContentLogicAgent	Reusable content transformation blocks
ComparisonLogicAgent	Rule-based product comparison
Template Agents	Define page structure (FAQ, Product, Comparison)
Orchestrator	Controls execution order (pipeline/DAG)

@Orchestration Diagram (System Design)
┌──────────────────┐
│ Raw Product Data │
└─────────┬────────┘
          ↓
┌──────────────────┐
│ Parser Agent     │
└─────────┬────────┘
          ↓
┌──────────────────┐
│ Question Agent   │
└─────────┬────────┘
          ↓
┌──────────────────┐
│ Content Logic    │
│ (Reusable Blocks)│
└─────────┬────────┘
          ↓
┌──────────────────┐
│ Templates        │
│ (FAQ/Product/Comp)│
└─────────┬────────┘
          ↓
┌──────────────────┐
│ Page Assembly    │
└─────────┬────────┘
          ↓
┌──────────────────┐
│ JSON Outputs     │
└──────────────────┘

@How to Run
python main.py


@Generated files:
output/
 ├── faq.json
 ├── product_page.json
 └── comparison_page.json
