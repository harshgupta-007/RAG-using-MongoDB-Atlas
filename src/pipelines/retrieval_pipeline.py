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


class RetrievalPipeline:

    def __init__(self):

        self.hybrid_search = HybridSearch()

        self.reranker = VoyageReranker()

        self.parent_retriever = ParentRetriever()

        self.context_builder = ContextBuilder()

    def retrieve(
        self,
        query: str,
        top_k: int = 10,
        rerank_k: int = 5
    ):

        # Step 1: Hybrid Search
        hybrid_result = (
            self.hybrid_search.search(
                query=query,
                k=top_k
            )
        )

        # Step 2: Rerank
        reranked_chunks = (
            self.reranker.rerank(
                query=query,
                documents=hybrid_result[
                    "hybrid_results"
                ],
                top_k=rerank_k
            )
        )

        # Step 3: Parent Retrieval
        parent_results = (
            self.parent_retriever.get_parents(
                reranked_chunks
            )
        )

        # Step 4: Context Building
        context = (
            self.context_builder.build_context(
                parent_results
            )
        )

        return {

            "query": query,

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
                context
        }