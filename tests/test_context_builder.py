from src.pipelines.retrieval_pipeline import (
    RetrievalPipeline
)

pipeline = RetrievalPipeline()

result = pipeline.retrieve(
    "What is aggregation pipeline?"
)

print(
    result["context"]
)