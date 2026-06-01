from src.retrieval.bm25_search import (
    BM25Search
)

bm25 = BM25Search()

results = bm25.search(
    "What is aggregation pipeline?"
)

for doc in results:

    print("=" * 80)

    print(doc["_id"])

    print(doc["bm25_score"])

    print(doc["metadata"])

    print(
        doc["chunk_text"][:300]
    )