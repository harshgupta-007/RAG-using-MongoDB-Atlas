from src.embedding.voyage_embedder import (
    VoyageEmbedder
)

from src.retrieval.vector_search import (
    AtlasVectorSearch
)
print("\nTESTING VECTOR SEARCH\n")
embedder = VoyageEmbedder()

retriever = AtlasVectorSearch()

query = (
    "What is aggregation pipeline?"
)

query_embedding = (
    embedder.embed_query(query)
)
print("\nQUERY EMBEDDING\n")
# print(query_embedding)
results = retriever.search(
    query_embedding,
    k=5
)
print("\nVECTOR SEARCH RESULTS\n")
# print(results)
for r in results:

    print("=" * 80)

    print(r["_id"])

    print(r["score"])

    print(r["metadata"])

    print(
        r["chunk_text"][:300]
    )