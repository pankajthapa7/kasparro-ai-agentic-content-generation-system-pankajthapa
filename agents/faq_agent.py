class FAQAgent:
    def run(self, state):
        faqs = []
        
        p_data = state.get("product", {})
        
        question_map = {
            "Usage": "How to Use",
            "Side Effects": "side_effects",
            "Benefits": "Benefits",
            "Concentration": "Concentration"
        }

        for category, data_key in question_map.items():
            
            answer = p_data.get(data_key, "Information not available")
            faqs.append({
                "category": category,
                "question": f"What is the {category.lower()} of this product?",
                "answer": answer
            })

        state["faq_page"] = {
            "page_type": "faq",
            "product": p_data.get("Product Name", "Unknown Product"),
            "price": p_data.get("Price", "N/A"),
            "faqs": faqs
        }
        return state