from src.query_understanding.llm_query_parser import (
    LLMQueryParser
)

from src.query_understanding.filter_generator import (
    FilterGenerator
)

from src.retrieval.hybrid_search import (
    HybridSearch
)

query = (
    "Show aggregation examples from Chapter 6"
)

parser = LLMQueryParser()

intent = parser.parse(query)

filters = (
    FilterGenerator()
    .generate(intent)
)

print("\nFILTERS\n")

print(filters)

results = (
    HybridSearch()
    .search(
        query=intent.search_query,
        filters=filters
    )
)

print("\nTOP RESULTS\n")

for doc in results[
    "hybrid_results"
][:5]:

    print("=" * 80)

    print(doc["_id"])

    print(doc["metadata"])