import voyageai

from src.config.settings import settings


class VoyageReranker:

    def __init__(self):

        self.client = voyageai.Client(
            api_key=settings.VOYAGE_API_KEY
        )

    def rerank(
        self,
        query,
        documents,
        top_k=5
    ):

        texts = [
            doc["chunk_text"]
            for doc in documents
        ]

        result = self.client.rerank(
            query=query,
            documents=texts,
            model="rerank-2",
            top_k=top_k
        )

        reranked_docs = []

        for item in result.results:

            doc = documents[
                item.index
            ]

            doc[
                "rerank_score"
            ] = item.relevance_score

            reranked_docs.append(
                doc
            )

        return reranked_docs