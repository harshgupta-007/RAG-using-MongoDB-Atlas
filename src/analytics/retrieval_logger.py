from datetime import datetime

from src.database.collections import (
    retrieval_logs_collection
)

from src.utils.logger import (
    logger
)


class RetrievalAnalytics:

    def log(
        self,
        retrieval_result,
        retrieval_time
    ):

        try:

            document = {

                "query":
                    retrieval_result["query"],

                "intent":
                    str(
                        retrieval_result[
                            "intent"
                        ]
                    ),

                "filters":
                    retrieval_result[
                        "filters"
                    ],

                "num_vector_results":
                    retrieval_result[
                        "num_vector_results"
                    ],

                "num_text_results":
                    retrieval_result[
                        "num_text_results"
                    ],

                "num_hybrid_results":
                    retrieval_result[
                        "num_hybrid_results"
                    ],

                "num_parent_documents":
                    retrieval_result[
                        "num_parent_documents"
                    ],

                "retrieval_time":
                    retrieval_time,

                "created_at":
                    datetime.utcnow()
            }

            retrieval_logs_collection.insert_one(
                document
            )

        except Exception:

            logger.exception(
                "Analytics Logging Failed"
            )