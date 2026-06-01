from src.pipelines.retrieval_pipeline import (
    RetrievalPipeline
)

pipeline = RetrievalPipeline()

result = pipeline.retrieve(
    "What is aggregation pipeline?"
)

print("\nRERANKED CHUNKS\n")

for doc in result["reranked_chunks"]:

    print(
        doc["_id"],
        doc["rerank_score"]
    )

print("\nPARENTS\n")

for doc in result["parent_documents"]:

    print(
        doc["_id"],
        doc["match_count"]
    )