from src.pipelines.retrieval_pipeline import (
    RetrievalPipeline
)

pipeline = RetrievalPipeline()

result = pipeline.retrieve(
    "What is aggregation pipeline?"
)

print("\nQUERY\n")

print(result["query"])

print("\nCHILD CHUNKS\n")

for chunk in result["child_chunks"]:

    print("=" * 80)

    print(chunk["_id"])

    print(chunk["parent_id"])

    print(chunk["score"])

    print(chunk["metadata"])

print("\nPARENT DOCUMENTS\n")

for parent in result["parent_documents"]:

    print("=" * 80)

    print(parent["_id"])

    print(parent["metadata"])

    print(parent["text"][:500])