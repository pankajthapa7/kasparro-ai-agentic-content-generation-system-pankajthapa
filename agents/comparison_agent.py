from data.fictional_product_b import PRODUCT_B

class ComparisonAgent:
    def run(self, state):
        # Product A is inside state['product']
        a = state.get("product", {})
        b = PRODUCT_B

        def get_ing_set(data, key):
            val = data.get(key, "")
            if isinstance(val, list): return set(val)
            return set([i.strip() for i in val.split(",") if i.strip()])

        ing_a = get_ing_set(a, "Key Ingredients")
        # Check if Product B uses "Key Ingredients" or "ingredients"
        ing_b = get_ing_set(b, "Key Ingredients") if "Key Ingredients" in b else get_ing_set(b, "ingredients")

        state["comparison_page"] = {
            "page_type": "comparison",
            "product_a": a.get("Product Name", "Product A"),
            "product_b": b.get("Product Name", b.get("name", "Product B")),
            "comparison": {
                "price": {
                    "a": a.get("Price", "N/A"),
                    "b": b.get("price", b.get("Price", "N/A"))
                },
                "common_ingredients": list(ing_a.intersection(ing_b))
            }
        }
        return state