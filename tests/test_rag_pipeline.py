from src.pipelines.rag_pipeline import (
    RAGPipeline
)

rag = RAGPipeline()

result = rag.ask(
    "What is aggregation pipeline?"
)

print("\nQUESTION\n")

print(result["question"])

print("\nANSWER\n")

print(result["answer"])

print("\nSOURCES\n")

for source in result["sources"]:

    print(
        source["_id"],
        source["metadata"]
    )