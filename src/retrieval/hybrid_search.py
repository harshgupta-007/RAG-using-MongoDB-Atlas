from src.embedding.voyage_embedder import (
    VoyageEmbedder
)

from src.retrieval.vector_search import (
    AtlasVectorSearch
)

from src.retrieval.atlas_text_search import (
    AtlasTextSearch
)

from src.retrieval.rrf import (
    ReciprocalRankFusion
)


class HybridSearch:

    def __init__(self):

        self.embedder = VoyageEmbedder()

        self.vector_search = (
            AtlasVectorSearch()
        )

        self.text_search = (
            AtlasTextSearch()
        )

        self.rrf = (
            ReciprocalRankFusion()
        )

    def search(
        self,
        query,
        k=10,
        filters=None
    ):

        query_embedding = (
            self.embedder.embed_query(
                query
            )
        )

        vector_results = (
            self.vector_search.search(
                query_embedding,
                k=k,
                filters=filters
            )
        )

        text_results = (
            self.text_search.search(
                query,
                k=k,
                filters=filters
            )
        )

        fused_results = (
            self.rrf.fuse(
                vector_results,
                text_results
            )
        )

        return {
            "vector_results": vector_results,
            "text_results": text_results,
            "hybrid_results": fused_results
        }