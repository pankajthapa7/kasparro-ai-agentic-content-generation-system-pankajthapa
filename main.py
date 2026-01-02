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
   
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    
    agents = {
        "parser": ParserAgent(),
        "question": QuestionAgent(),
        "faq": FAQAgent(),
        "product_page": ProductPageAgent(),
        "comparison": ComparisonAgent()
    }

    
    orchestrator = Orchestrator(agents)
    print("--- Executing Agentic System ---")
    pages = orchestrator.run(RAW_PRODUCT_DATA)

   
    for filename, content in pages.items():
        file_path = os.path.join(output_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            
            page_key = filename.replace(".json", "")
            
           
            data_to_save = content.get(page_key) if isinstance(content, dict) and page_key in content else content
            
            json.dump(data_to_save, f, indent=2, ensure_ascii=False)
            print(f"File created: {file_path}")

    print("\n[SUCCESS] All agents finished. Check the 'output' folder.")

if __name__ == "__main__":
    main()