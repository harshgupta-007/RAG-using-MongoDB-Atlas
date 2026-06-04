# MongoDB Atlas RAG System

A production-style Retrieval-Augmented Generation (RAG) application built using MongoDB Atlas Search, MongoDB Atlas Vector Search, Voyage AI, Gemini, and Streamlit.

The system supports query understanding, metadata-aware retrieval, hybrid search, reranking, parent-child retrieval, persistent chat sessions, retrieval analytics, and monitoring dashboards.

---

# Features

## Retrieval

* MongoDB Atlas Vector Search
* MongoDB Atlas Text Search
* Hybrid Search using Reciprocal Rank Fusion (RRF)
* Voyage AI Embeddings
* Voyage AI Reranking
* Parent-Child Retrieval Architecture

## Query Understanding

* Gemini-powered Intent Extraction
* Metadata Filter Generation
* Chapter-aware Retrieval
* Structured Query Parsing

## Context Construction

* Parent Document Retrieval
* Context Aggregation
* Metadata-aware Context Building

## Chat Experience

* Persistent Chat Sessions
* MongoDB Chat History Storage
* Auto-generated Chat Titles
* ChatGPT-style Interface

## Monitoring & Analytics

* Retrieval Debug Dashboard
* System Information Dashboard
* Analytics Dashboard
* Centralized Logging
* Retrieval Analytics Collection

## Production Features

* Structured Logging
* Error Handling
* Analytics Logging
* Modular Architecture

---

# Architecture

Detailed architecture documentation is available in:

```text
docs/architecture.md
```

High-Level Flow:

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

# Project Structure

```text
mongodb-atlas-rag/

├── app/
│   ├── Home.py
│   └── pages/
│       ├── 1_Chat.py
│       ├── 2_Retrieval_Debug.py
│       ├── 3_System_Info.py
│       └── 4_Analytics.py
│
├── src/
│   ├── analytics/
│   ├── chat/
│   ├── config/
│   ├── database/
│   ├── embedding/
│   ├── generation/
│   ├── pipelines/
│   ├── prompts/
│   ├── query_understanding/
│   ├── retrieval/
│   ├── reranking/
│   └── utils/
│
├── tests/
│
├── docs/
│   └── architecture.md
│
├── logs/
│
├── README.md
├── requirements.txt
└── .env
```

---

# Tech Stack

## Database

* MongoDB Atlas

## Search

* MongoDB Atlas Search
* MongoDB Atlas Vector Search

## Embeddings

* Voyage AI

## Reranking

* Voyage AI Reranker

## Large Language Model

* Gemini 2.5 Flash Lite

## Frontend

* Streamlit

## Backend

* Python

## Analytics

* MongoDB Aggregation Framework

---

# Setup Instructions

## Clone Repository

```bash
git clone <repository_url>

cd mongodb-atlas-rag
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
MONGO_URI=

DATABASE_NAME=

VOYAGE_API_KEY=

GEMINI_API_KEY=
```

---

# MongoDB Atlas Indexes

## Vector Search Index

```text
vector_index
```

Used for semantic retrieval using Voyage embeddings.

## Atlas Search Index

```text
text_index
```

Used for keyword-based retrieval and metadata filtering.

---

# Application Pages

## Chat

Interactive RAG chatbot with:

* Persistent chat sessions
* Auto-generated titles
* Retrieval-augmented responses

---

## Retrieval Debug

Inspect every stage of retrieval:

* Query Understanding
* Metadata Filters
* Vector Results
* Text Results
* Hybrid Results
* Reranked Results
* Parent Documents
* Final Context

---

## System Information

Monitor:

* MongoDB Connectivity
* Collection Statistics
* Model Information
* Environment Information

---

## Analytics Dashboard

Track:

* Total Searches
* Retrieval Performance
* Top Intents
* Recent Searches

---

# MongoDB Collections

## parent_documents

Stores parent-level documents.

## child_chunks

Stores chunked documents for retrieval.

## chat_sessions

Stores user chat sessions.

## chat_messages

Stores chat history.

## retrieval_logs

Stores retrieval analytics and monitoring data.

---

# Logging

Application logs are stored in:

```text
logs/rag.log
```

Logs include:

* Query Processing
* Retrieval Metrics
* Generation Events
* Error Tracking

---

# Analytics

The system automatically tracks:

* Query
* Intent
* Filters
* Retrieval Counts
* Retrieval Duration
* Search Activity

Example:

```json
{
  "query": "Show aggregation examples from Chapter 6",
  "intent": "search_examples",
  "retrieval_time": 2.45
}
```

---

# Running the Application

```bash
streamlit run app/Home.py
```

---

# Future Improvements

* Docker Deployment
* Authentication & User Management
* Multi-Document Support
* Citation Generation
* Evaluation Framework
* Agentic Retrieval
* Feedback Collection
* LLM Caching
* Conversation Memory
* Multi-Modal Retrieval

---

# Author

Harsh Gupta

Senior Analyst | AI/ML Engineer

Skills:

* Python
* MongoDB
* Machine Learning
* Retrieval-Augmented Generation (RAG)
* Streamlit
* Voyage AI
* Gemini
* Data Analytics
* AWS

```
```
