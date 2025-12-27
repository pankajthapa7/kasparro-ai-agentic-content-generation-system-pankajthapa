class QuestionGenerationAgent:
    def run(self, product):
        return {
            "Informational": [
                f"What is {product.name}?",
                f"Who should use {product.name}?",
                "What skin types is it suitable for?"
            ],
            "Usage": [
                "How do I use this product?",
                "When should it be applied?",
                "Can it be used daily?"
            ],
            "Safety": [
                "Are there any side effects?",
                "Is tingling normal?",
                "Is it suitable for sensitive skin?"
            ],
            "Ingredients": [
                "What are the key ingredients?",
                "What does Vitamin C do?",
                "What does Hyaluronic Acid do?"
            ],
            "Purchase": [
                "What is the price?",
                "Is it worth the price?",
                "Who should buy this product?"
            ]
        }
