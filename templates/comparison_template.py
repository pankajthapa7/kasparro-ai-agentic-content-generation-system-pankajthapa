class ComparisonTemplate:
    def render(self, product_a, product_b, comparison_logic):
        return {
            "page_type": "comparison",
            "products": {
                "product_a": {
                    "name": product_a.name,
                    "ingredients": product_a.ingredients,
                    "benefits": product_a.benefits,
                    "price": product_a.price
                },
                "product_b": product_b
            },
            "comparison": {
                "price": comparison_logic.compare_price(product_a, product_b),
                "ingredients": comparison_logic.compare_ingredients(product_a, product_b),
                "benefits": comparison_logic.compare_benefits(product_a, product_b)
            }
        }
