from src.pipelines.retrieval_pipeline import (
    RetrievalPipeline
)

pipeline = RetrievalPipeline()

result = pipeline.retrieve(
    "Show aggregation examples from Chapter 6"
)

print("\nINTENT\n")

print(
    result["intent"]
)

print("\nFILTERS\n")

print(
    result["filters"]
)

print("\nPARENTS\n")

for doc in result[
    "parent_documents"
]:

    print(
        doc["_id"]
    )

    print(
        doc["metadata"]
    )

    print()