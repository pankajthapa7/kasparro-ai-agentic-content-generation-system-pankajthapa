from agents.product_parser_agent import ProductParserAgent
from agents.question_generation_agent import QuestionGenerationAgent
from agents.content_logic_agent import ContentLogicAgent
from agents.comparison_logic_agent import ComparisonLogicAgent
from agents.page_assembly_agent import PageAssemblyAgent

from templates.faq_template import FAQTemplate
from templates.product_page_template import ProductPageTemplate
from templates.comparison_template import ComparisonTemplate

from data.fictional_product_b import PRODUCT_B

class Orchestrator:
    def run(self, raw_data):
        parser = ProductParserAgent()
        question_agent = QuestionGenerationAgent()
        logic_agent = ContentLogicAgent()
        comparison_logic = ComparisonLogicAgent()
        assembler = PageAssemblyAgent()

        product = parser.run(raw_data)
        questions = question_agent.run(product)

        return {
            "faq.json": assembler.assemble(
                FAQTemplate().render(product, questions, logic_agent)
            ),
            "product_page.json": assembler.assemble(
                ProductPageTemplate().render(product, logic_agent)
            ),
            "comparison_page.json": assembler.assemble(
                ComparisonTemplate().render(product, PRODUCT_B, comparison_logic)
            )
        }
