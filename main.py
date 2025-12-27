import json
import os
from agents.orchestrator import Orchestrator

RAW_PRODUCT_DATA = {
    "Product Name": "GlowBoost Vitamin C Serum",
    "Concentration": "10% Vitamin C",
    "Skin Type": "Oily, Combination",
    "Key Ingredients": "Vitamin C, Hyaluronic Acid",
    "Benefits": "Brightening, Fades dark spots",
    "How to Use": "Apply 2–3 drops in the morning before sunscreen",
    "Side Effects": "Mild tingling for sensitive skin",
    "Price": "₹699"
}

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)

    orchestrator = Orchestrator()
    outputs = orchestrator.run(RAW_PRODUCT_DATA)

    for filename, content in outputs.items():
        with open(f"output/{filename}", "w", encoding="utf-8") as f:
            json.dump(content, f, indent=2, ensure_ascii=False)

    print("✅ All pages generated successfully")
