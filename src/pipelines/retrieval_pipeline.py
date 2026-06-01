from src.retrieval.hybrid_search import (
    HybridSearch
)

from src.reranking.voyage_reranker import (
    VoyageReranker
)

from src.retrieval.parent_retriever import (
    ParentRetriever
)

from src.retrieval.context_builder import (
    ContextBuilder
)
from src.query_understanding.llm_query_parser import (
    LLMQueryParser
)

from src.query_understanding.filter_generator import (
    FilterGenerator
)

class RetrievalPipeline:

    def __init__(self):

        self.query_parser = (
            LLMQueryParser()
        )

        self.filter_generator = (
            FilterGenerator()
        )

        self.hybrid_search = (
            HybridSearch()
        )

        self.reranker = (
            VoyageReranker()
        )

        self.parent_retriever = (
            ParentRetriever()
        )

        self.context_builder = (
            ContextBuilder()
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 10,
        rerank_k: int = 5
    ):

        # Step 1: Query Understanding

        intent = (
            self.query_parser.parse(
                query
            )
        )

        # Step 2: Filter Generation

        filters = (
            self.filter_generator.generate(
                intent
            )
        )

        # Step 3: Hybrid Search

        hybrid_result = (
            self.hybrid_search.search(
                query=query,
                k=top_k,
                filters=filters
            )
        )

        # Step 4: Rerank
        reranked_chunks = (
            self.reranker.rerank(
                query=query,
                documents=hybrid_result[
                    "hybrid_results"
                ],
                top_k=rerank_k
            )
        )

        # Step 5: Parent Retrieval
        parent_results = (
            self.parent_retriever.get_parents(
                reranked_chunks
            )
        )

        # Step 6: Context Building
        context = (
            self.context_builder.build_context(
                parent_results
            )
        )

        return {

            "query": query,

            "intent":
                intent,
            "filters":
                filters,

            "num_vector_results":
                len(
                    hybrid_result[
                        "vector_results"
                    ]
                ),

            "num_text_results":
                len(
                    hybrid_result[
                        "text_results"
                    ]
                ),

            "num_hybrid_results":
                len(
                    hybrid_result[
                        "hybrid_results"
                    ]
                ),

            "num_parent_documents":
                len(parent_results),

            "vector_results":
                hybrid_result[
                    "vector_results"
                ],

            "text_results":
                hybrid_result[
                    "text_results"
                ],

            "hybrid_results":
                hybrid_result[
                    "hybrid_results"
                ],

            "reranked_chunks":
                reranked_chunks,

            "parent_documents":
                parent_results,

            "context":
                context,


        }


