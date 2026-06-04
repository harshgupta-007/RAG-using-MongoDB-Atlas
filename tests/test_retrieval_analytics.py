from src.pipelines.retrieval_pipeline import (
    RetrievalPipeline
)

pipeline = (
    RetrievalPipeline()
)

pipeline.retrieve(
    "Show aggregation examples from Chapter 6"
)

print(
    "Analytics Logged"
)