class FAQTemplate:
    def render(self, product, questions, logic_agent):
        faqs = []

        for category, qs in questions.items():
            faqs.append({
                "category": category,
                "question": qs[0],
                "answer": (
                    product.usage
                    if category == "Usage"
                    else product.side_effects
                )
            })

        return {
            "page_type": "faq",
            "product": product.name,
            "faqs": faqs
        }
