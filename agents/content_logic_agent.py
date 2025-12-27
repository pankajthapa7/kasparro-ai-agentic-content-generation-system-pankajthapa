class ContentLogicAgent:

    def generate_benefits_block(self, product):
        return product.benefits

    def generate_usage_block(self, product):
        return {
            "instructions": product.usage,
            "recommended_time": "Morning"
        }

    def generate_safety_block(self, product):
        return {
            "side_effects": product.side_effects,
            "notes": "Patch test recommended for sensitive skin"
        }

    def generate_ingredient_block(self, product):
        return product.ingredients
