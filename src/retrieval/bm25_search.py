from rank_bm25 import BM25Okapi

from src.database.collections import (
    child_collection
)


class BM25Search:

    def __init__(self):

        self.documents = list(
            child_collection.find({})
        )

        self.corpus = [
            doc["chunk_text"].split()
            for doc in self.documents
        ]

        self.bm25 = BM25Okapi(
            self.corpus
        )

    def search(
        self,
        query,
        k=5
    ):

        tokenized_query = (
            query.split()
        )

        scores = self.bm25.get_scores(
            tokenized_query
        )

        ranked = sorted(
            zip(
                self.documents,
                scores
            ),
            key=lambda x: x[1],
            reverse=True
        )

        results = []

        for doc, score in ranked[:k]:

            doc["bm25_score"] = (
                float(score)
            )

            results.append(doc)

        return results