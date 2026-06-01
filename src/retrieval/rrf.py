from collections import defaultdict


class ReciprocalRankFusion:

    def fuse(
        self,
        vector_results,
        text_results,
        k=60
    ):

        scores = defaultdict(float)
        documents = {}

        # Vector ranking
        for rank, doc in enumerate(
            vector_results,
            start=1
        ):

            doc_id = doc["_id"]

            scores[doc_id] += (
                1 / (k + rank)
            )

            documents[doc_id] = doc

        # Text ranking
        for rank, doc in enumerate(
            text_results,
            start=1
        ):

            doc_id = doc["_id"]

            scores[doc_id] += (
                1 / (k + rank)
            )

            documents[doc_id] = doc

        fused_results = []

        for doc_id, score in scores.items():

            doc = documents[doc_id]

            doc["rrf_score"] = score

            fused_results.append(doc)

        fused_results.sort(
            key=lambda x: x["rrf_score"],
            reverse=True
        )

        return fused_results