class QuestionAgent:
    def run(self, state):
        p = state["product"]["name"]
        state["questions"] = {
            "Usage": [f"How do I use {p}?"],
            "Safety": ["Are there any side effects?"],
            "Ingredients": ["What are the key ingredients?"],
            "Purchase": ["What is the price?"],
            "General": [f"What is {p}?"]
        }
        return state
