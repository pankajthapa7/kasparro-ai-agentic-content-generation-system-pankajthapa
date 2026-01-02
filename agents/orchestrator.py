class Orchestrator:
    def __init__(self, agents: dict):
        self.agents = agents

    def run(self, raw_product_data: dict) -> dict:
        state = {}

        
        state["product"] = self.agents["parser"].run(raw_product_data)
        state["questions"] = self.agents["question"].run(state["product"])

       
        state = self.agents["faq"].run(state)
        state = self.agents["product_page"].run(state)
        state = self.agents["comparison"].run(state)

        
        return {
            "faq_page.json": state.get("faq_page"),
            "product_page.json": state.get("product_page"),
            "comparison_page.json": state.get("comparison_page")
        }