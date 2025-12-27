class ComparisonLogicAgent:

    def compare_price(self, product_a, product_b):
        return {
            "product_a_price": product_a.price,
            "product_b_price": product_b["price"]
        }

    def compare_ingredients(self, product_a, product_b):
        overlap = set(product_a.ingredients).intersection(set(product_b["ingredients"]))

        return {
            "common_ingredients": list(overlap),
            "product_a_unique": list(set(product_a.ingredients) - overlap),
            "product_b_unique": list(set(product_b["ingredients"]) - overlap)
        }

    def compare_benefits(self, product_a, product_b):
        return {
            "product_a_benefits": product_a.benefits,
            "product_b_benefits": product_b["benefits"]
        }
