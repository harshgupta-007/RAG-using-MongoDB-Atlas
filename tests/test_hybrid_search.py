from src.retrieval.hybrid_search import (
    HybridSearch
)

hybrid = HybridSearch()

results = hybrid.search(
    "What is aggregation pipeline?"
)

for doc in results[:5]:

    print("=" * 80)

    print(doc["_id"])

    print(doc["rrf_score"])

    print(doc["metadata"])

    print(
        doc["chunk_text"][:250]
    )