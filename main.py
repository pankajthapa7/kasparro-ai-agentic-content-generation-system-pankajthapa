import json
import os

from agents.orchestrator import Orchestrator
from agents.parser_agent import ParserAgent
from agents.question_agent import QuestionAgent
from agents.faq_agent import FAQAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent

RAW_PRODUCT_DATA = {
    "Product Name": "GlowBoost Vitamin C Serum",
    "Concentration": "10% Vitamin C",
    "Skin Type": "Oily, Combination",
    "Key Ingredients": "Vitamin C, Hyaluronic Acid",
    "Benefits": "Brightening, Fades dark spots",
    "How to Use": "Apply 2–3 drops in the morning before sunscreen",
    "side_effects": "Mild tingling for sensitive skin",
    "Price": "₹699"
}

def main():
    # 1. Recreate the output directory
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # 2. Initialize Agents
    agents = {
        "parser": ParserAgent(),
        "question": QuestionAgent(),
        "faq": FAQAgent(),
        "product_page": ProductPageAgent(),
        "comparison": ComparisonAgent()
    }

    # 3. Run Orchestrator
    orchestrator = Orchestrator(agents)
    print("--- Executing Agentic System ---")
    pages = orchestrator.run(RAW_PRODUCT_DATA)

    # 4. Save the results
    # Your Orchestrator returns a dict where key=filename, value=content
    for filename, content in pages.items():
        file_path = os.path.join(output_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            # We save the specific page inside the content dictionary
            # Example: from content["faq_page"]
            page_key = filename.replace(".json", "")
            
            # Use the specific page key if it exists, otherwise dump the whole content
            data_to_save = content.get(page_key) if isinstance(content, dict) and page_key in content else content
            
            json.dump(data_to_save, f, indent=2, ensure_ascii=False)
            print(f"File created: {file_path}")

    print("\n[SUCCESS] All agents finished. Check the 'output' folder.")

if __name__ == "__main__":
    main()