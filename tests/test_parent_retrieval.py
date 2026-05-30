from src.embedding.voyage_embedder import (
    VoyageEmbedder
)

from src.retrieval.vector_search import (
    AtlasVectorSearch
)

from src.retrieval.parent_retriever import (
    ParentRetriever
)

embedder = VoyageEmbedder()

retriever = AtlasVectorSearch()

parent_retriever = ParentRetriever()

query = (
    "What is aggregation pipeline?"
)

query_embedding = (
    embedder.embed_query(query)
)

chunks = retriever.search(
    query_embedding,
    k=5
)

parents = (
    parent_retriever.get_parents(
        chunks
    )
)

print(
    f"Parents Found: {len(parents)}"
)

for parent in parents:

    print("=" * 80)

    print(parent["_id"])

    print(
        "MATCH COUNT:",
        parent["match_count"]
    )

    print(parent["metadata"])