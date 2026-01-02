class Orchestrator:
    def __init__(self, agents: dict):
        self.agents = agents

    def run(self, raw_product_data: dict) -> dict:
        state = {}

        # 1. Prepare base data
        state["product"] = self.agents["parser"].run(raw_product_data)
        state["questions"] = self.agents["question"].run(state["product"])

        # 2. Sequential update of state (Each agent adds its piece to the state)
        state = self.agents["faq"].run(state)
        state = self.agents["product_page"].run(state)
        state = self.agents["comparison"].run(state)

        # 3. Return the specific results with their intended filenames
        return {
            "faq_page.json": state.get("faq_page"),
            "product_page.json": state.get("product_page"),
            "comparison_page.json": state.get("comparison_page")
        }