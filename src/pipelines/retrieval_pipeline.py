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
from src.utils.logger import (
    logger
)
import time
from src.utils.exceptions import (
    RetrievalError
)

from src.analytics.retrieval_logger import (
    RetrievalAnalytics
)
start_time = time.time()


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

        self.analytics = (
            RetrievalAnalytics()
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 10,
        rerank_k: int = 5
    ):
        try:
            start_time = time.time()

            logger.info(
                f"Query Received: {query}"
            )
            # Step 1: Query Understanding

            intent = (
                self.query_parser.parse(
                    query
                )
            )
            logger.info(
                f"Intent Parsed: {intent}"
            )

            # Step 2: Filter Generation

            filters = (
                self.filter_generator.generate(
                    intent
                )
            )
            logger.info(
                f"Filters Generated: {filters}"
            )

            # Step 3: Hybrid Search

            hybrid_result = (
                self.hybrid_search.search(
                    query=query,
                    k=top_k,
                    filters=filters
                )
            )
            logger.info(
                f"Vector Results: "
                f"{len(hybrid_result['vector_results'])}"
            )

            logger.info(
                f"Text Results: "
                f"{len(hybrid_result['text_results'])}"
            )

            logger.info(
                f"Hybrid Results: "
                f"{len(hybrid_result['hybrid_results'])}"
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

            logger.info(
                f"Reranked Chunks: "
                f"{len(reranked_chunks)}"
            )

            # Step 5: Parent Retrieval
            parent_results = (
                self.parent_retriever.get_parents(
                    reranked_chunks
                )
            )
            logger.info(
                f"Parent Documents: "
                f"{len(parent_results)}"
            )

            # Step 6: Context Building
            context = (
                self.context_builder.build_context(
                    parent_results
                )
            )

            logger.info(
                f"Context Built | Characters={len(context)}"
            )
            logger.info(
                "Retrieval Pipeline Complete"
            )
            # retrieval logic

            logger.info(
                f"Retrieval Duration: "
                f"{round(time.time()-start_time, 2)}s"
            )

            retrieval_time = round(
                time.time() - start_time,
                2
            )
            logger.info(
                f"Retrieval Duration: "
                f"{retrieval_time}s"
            )
            result = {

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
            self.analytics.log(
                result,
                retrieval_time
            )

            return result
        
        except Exception as e:

            logger.exception(
                "Retrieval Pipeline Failed"
            )

            raise RetrievalError(
                str(e)
            )


