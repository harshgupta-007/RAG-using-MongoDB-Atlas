from src.pipelines.rag_pipeline import (
    RAGPipeline
)

pipeline = RAGPipeline()

result = pipeline.ask(
    "Show aggregation examples from Chapter 6"
)

print("\nQUESTION\n")
print(result["question"])

print("\nINTENT\n")
print(result["intent"])

print("\nFILTERS\n")
print(result["filters"])

print("\nANSWER\n")
print(result["answer"])

print("\nSOURCES\n")

for source in result["sources"]:

    print(
        source["_id"]
    )

    print(
        source["metadata"]
    )

    print()