import streamlit as st

st.set_page_config(
    page_title="MongoDB Atlas RAG",
    page_icon="🤖",
    layout="wide"
)

st.title(
    "MongoDB Atlas RAG System"
)

st.markdown(
    """
    Production-grade RAG system built with:

    - MongoDB Atlas Vector Search
    - Atlas Text Search
    - Hybrid Search (RRF)
    - Voyage Embeddings
    - Voyage Reranking
    - Parent-Child Retrieval
    - Metadata Filtering
    - Gemini Generation
    """
)