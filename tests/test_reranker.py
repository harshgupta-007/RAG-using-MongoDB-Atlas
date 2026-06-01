from src.retrieval.hybrid_search import (
    HybridSearch
)

from src.reranking.voyage_reranker import (
    VoyageReranker
)

query = (
    "What is aggregation pipeline?"
)

hybrid = HybridSearch()

reranker = VoyageReranker()

results = hybrid.search(query)

reranked = reranker.rerank(
    query,
    results["hybrid_results"]
)

for doc in reranked:

    print("=" * 80)

    print(doc["_id"])

    print(doc["rerank_score"])

    print(doc["metadata"])