from src.pipelines.retrieval_pipeline import (
    RetrievalPipeline
)

from src.generation.gemini_generator import (
    GeminiGenerator
)


class RAGPipeline:

    def __init__(self):

        self.retrieval = (
            RetrievalPipeline()
        )

        self.generator = (
            GeminiGenerator()
        )

    def ask(
        self,
        question
    ):

        retrieval_result = (
            self.retrieval.retrieve(
                question
            )
        )

        answer = (
            self.generator.generate_answer(
                question,
                retrieval_result["context"]
            )
        )

        return {

            "question":
                question,

            "answer":
                answer,

            "context":
                retrieval_result["context"],

            "sources":
                retrieval_result[
                    "parent_documents"
                ]
        }