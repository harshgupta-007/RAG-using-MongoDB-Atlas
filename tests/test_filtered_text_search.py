from src.retrieval.atlas_text_search import (
    AtlasTextSearch
)

filters = {
    "metadata.chapter_number": 6
}

results = (
    AtlasTextSearch()
    .search(
        query="aggregation",
        filters=filters
    )
)

print(
    f"\nResults Found: {len(results)}\n"
)

for doc in results:

    print(doc["_id"])

    print(doc["metadata"])

    print()