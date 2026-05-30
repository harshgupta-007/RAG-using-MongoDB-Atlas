from src.embedding.voyage_embedder import (
    VoyageEmbedder
)

from src.retrieval.vector_search import (
    AtlasVectorSearch
)

from src.retrieval.parent_retriever import (
    ParentRetriever
)

from src.retrieval.context_builder import (
    ContextBuilder
)


class RetrievalPipeline:

    def __init__(self):

        self.embedder = VoyageEmbedder()

        self.vector_search = AtlasVectorSearch()

        self.parent_retriever = ParentRetriever()

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):
        self.context_builder = (
            ContextBuilder()
        )

        # Step 1
        query_embedding = (
            self.embedder.embed_query(query)
        )

        # Step 2
        child_results = (
            self.vector_search.search(
                query_embedding,
                k=top_k
            )
        )

        # Step 3
        parent_results = (
            self.parent_retriever.get_parents(
                child_results
            )
        )

        context = (
            self.context_builder
            .build_context(
                parent_results
            )
        )

        return {
            "query": query,

            "num_child_chunks":
                len(child_results),

            "num_parent_documents":
                len(parent_results),

            "child_chunks":
                child_results,

            "parent_documents":
                parent_results,

            "context":
                context
        }