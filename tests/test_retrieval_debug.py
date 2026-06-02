# tests/test_retrieval_debug.py

from pprint import pprint

from src.pipelines.retrieval_pipeline import (
    RetrievalPipeline
)

result = (
    RetrievalPipeline()
    .retrieve(
        "show aggregation examples from chapter 6"
    )
)

pprint(result.keys())