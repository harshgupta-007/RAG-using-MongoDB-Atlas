# MongoDB Atlas RAG System Architecture

## High-Level Flow

```text
User
 │
 ▼
Streamlit Chat UI
 │
 ▼
RAG Pipeline
 │
 ├── Query Understanding (Gemini)
 │
 ├── Filter Generator
 │
 ├── Atlas Vector Search
 │
 ├── Atlas Text Search
 │
 ├── Hybrid Search (RRF)
 │
 ├── Voyage Reranker
 │
 ├── Parent Retriever
 │
 └── Context Builder
 │
 ▼
Gemini Generator
 │
 ▼
Final Answer
```

---

## Query Understanding Layer

Purpose:

* Detect user intent
* Extract metadata filters
* Generate optimized retrieval query

Example:

```text
Show aggregation examples from Chapter 6
```

Output:

```json
{
  "intent": "search_examples",
  "chapter": "6",
  "search_query": "aggregation"
}
```

---

## Metadata Filter Generation

Purpose:

Convert parsed intent into MongoDB Atlas Search filters.

Example:

```json
{
  "metadata.chapter_number": 6
}
```

---

## Hybrid Retrieval Layer

### Vector Search

Uses:

* Voyage Embeddings
* MongoDB Atlas Vector Search

Purpose:

Retrieve semantically similar chunks.

---

### Text Search

Uses:

* MongoDB Atlas Search

Purpose:

Retrieve keyword matches.

---

### Hybrid Search

Uses:

* Reciprocal Rank Fusion (RRF)

Purpose:

Combine vector and text results.

---

## Reranking Layer

Uses:

* Voyage Reranker

Purpose:

Improve ranking quality before context creation.

---

## Parent Retrieval Layer

Purpose:

Convert child chunks into parent documents.

Output:

```json
{
  "_id": "parent_41",
  "match_count": 3
}
```

---

## Context Builder

Purpose:

Construct final context passed to the LLM.

---

## Generation Layer

Uses:

* Gemini 2.5 Flash Lite

Purpose:

Generate final response using retrieved context.

---

## Chat System

Collections:

* chat_sessions
* chat_messages

Features:

* Persistent conversations
* Auto-generated chat titles

---

## Analytics System

Collection:

* retrieval_logs

Tracks:

* Query
* Intent
* Filters
* Retrieval Time
* Retrieval Counts

---

## Monitoring

Features:

* Application Logging
* Retrieval Debug Page
* System Info Dashboard
* Analytics Dashboard

```
```
