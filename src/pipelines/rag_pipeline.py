from src.pipelines.retrieval_pipeline import (
    RetrievalPipeline
)

from src.generation.gemini_generator import (
    GeminiGenerator
)

from src.utils.logger import (
    logger
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
        try:

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

                "intent":
                    retrieval_result[
                        "intent"
                    ],

                "filters":
                    retrieval_result[
                        "filters"
                    ],

                "sources":
                    retrieval_result[
                        "parent_documents"
                    ],

                "context":
                    retrieval_result[
                        "context"
                    ],

                "retrieval":
                    retrieval_result
            }
        
        except Exception as e:

            logger.exception(
                "RAG Pipeline Failed"
            )

            raise