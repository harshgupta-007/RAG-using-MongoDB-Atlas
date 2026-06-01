from src.query_understanding.query_classifier import (
    QueryClassifier
)

from src.query_understanding.metadata_filter_builder import (
    MetadataFilterBuilder
)

query = (
    "Show aggregation examples from Chapter 6"
)

classifier = QueryClassifier()

builder = MetadataFilterBuilder()

print(
    classifier.classify(query)
)

print(
    builder.build(query)
)