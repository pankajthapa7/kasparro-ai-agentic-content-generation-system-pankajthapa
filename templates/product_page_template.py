class ProductPageTemplate:
    def render(self, product, logic_agent):
        return {
            "page_type": "product",
            "name": product.name,
            "concentration": product.concentration,
            "skin_type": product.skin_types,
            "description": f"{product.name} is a {product.concentration} Vitamin C serum.",
            "key_ingredients": logic_agent.generate_ingredient_block(product),
            "benefits": logic_agent.generate_benefits_block(product),
            "usage": logic_agent.generate_usage_block(product),
            "safety": logic_agent.generate_safety_block(product),
            "price": product.price
        }
