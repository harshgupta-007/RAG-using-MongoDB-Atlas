from src.ingestion.ingest_to_mongodb import (
    MongoDBIngestion
)

ingestor = MongoDBIngestion()

ingestor.ingest_parents(
    "data/processed/parent_documents.json"
)

ingestor.ingest_children(
    "data/processed/embedded_chunks.json"
)