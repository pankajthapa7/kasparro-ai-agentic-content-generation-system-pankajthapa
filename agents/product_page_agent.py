class ProductPageAgent:
    def run(self, state):
        p_data = state.get("product", {})
        name = p_data.get("Product Name", "Unknown Product")
        
        state["product_page"] = {
            "page_type": "product",
            "name": name,
            "description": f"{name} is a {p_data.get('Concentration', 'N/A')} formula.",
            "ingredients": p_data.get("Key Ingredients", "N/A"),
            "benefits": p_data.get("Benefits", "N/A"),
            "usage": p_data.get("How to Use", "N/A"),
            "side_effects": p_data.get("side_effects", "N/A"),
            "price": p_data.get("Price", "N/A")
        }
        return state