from src.database.collections import (
    child_collection
)
class AtlasTextSearch:

    def search(
        self,
        query,
        k=10,
        filters=None
    ):

        if filters:

            chapter_number = (
                filters.get(
                    "metadata.chapter_number"
                )
            )
            pipeline = [
                {
                    "$search": {
                        "index": "text_index",
                        "compound": {
                            "must": [
                                {
                                    "text": {
                                        "query": query,
                                        "path": "chunk_text"
                                    }
                                }
                            ],
                            "filter": [
                                {
                                    "equals": {
                                        "path": "metadata.chapter_number",
                                        "value": chapter_number
                                    }
                                }
                            ]
                        }
                    }
                },
                {
                    "$limit": k
                },
                {
                    "$project": {
                        "_id": 1,
                        "parent_id": 1,
                        "chunk_text": 1,
                        "metadata": 1,
                        "score": {
                            "$meta": "searchScore"
                        }
                    }
                }
            ]

        else:

            pipeline = [
                {
                    "$search": {
                        "index": "text_index",
                        "text": {
                            "query": query,
                            "path": "chunk_text"
                        }
                    }
                },
                {
                    "$limit": k
                },
                {
                    "$project": {
                        "_id": 1,
                        "parent_id": 1,
                        "chunk_text": 1,
                        "metadata": 1,
                        "score": {
                            "$meta": "searchScore"
                        }
                    }
                }
            ]
        return list(
            child_collection.aggregate(
                pipeline
            )
        )