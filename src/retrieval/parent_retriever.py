from collections import Counter

from src.database.collections import (
    parent_collection
)


class ParentRetriever:

    def get_parents(
        self,
        child_results
    ):

        # Collect parent ids
        parent_ids = [
            doc["parent_id"]
            for doc in child_results
        ]

        # Count occurrences
        counts = Counter(parent_ids)

        # Sort by frequency
        sorted_parents = sorted(
            counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        parent_docs = []

        for parent_id, match_count in sorted_parents:

            parent_doc = parent_collection.find_one(
                {"_id": parent_id}
            )

            if parent_doc:

                parent_doc[
                    "match_count"
                ] = match_count

                parent_docs.append(
                    parent_doc
                )

        return parent_docs