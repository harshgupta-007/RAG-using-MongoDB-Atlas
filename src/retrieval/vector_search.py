from src.database.collections import child_collection
from src.config.settings import settings


class AtlasVectorSearch:

    def search(
        self,
        query_embedding,
        k=5
    ):

        pipeline = [
            {
                "$vectorSearch": {
                    "index":
                        settings.VECTOR_INDEX_NAME,

                    "path":
                        "embedding",

                    "queryVector":
                        query_embedding,

                    "numCandidates":
                        20,

                    "limit":
                        k
                }
            },
            {
                "$project": {
                    "_id": 1,
                    "parent_id": 1,
                    "chunk_text": 1,
                    "metadata": 1,
                    "score": {
                        "$meta":
                            "vectorSearchScore"
                    }
                }
            }
        ]

        return list(
            child_collection.aggregate(
                pipeline
            )
        )