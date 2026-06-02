import sys
from pathlib import Path

ROOT_DIR = (
    Path(__file__)
    .resolve()
    .parents[2]
)

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import streamlit as st

from src.pipelines.retrieval_pipeline import (
    RetrievalPipeline
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Retrieval Debug",
    page_icon="🔍",
    layout="wide"
)

st.title(
    "🔍 Retrieval Debug"
)

st.markdown(
    """
Inspect every stage of the retrieval pipeline:

- Query Understanding
- Metadata Filtering
- Vector Search
- Text Search
- Hybrid Search
- Reranking
- Parent Retrieval
- Final Context
"""
)

# =====================================================
# QUERY INPUT
# =====================================================

query = st.text_input(
    "Enter Query",
    placeholder="Show aggregation examples from Chapter 6"
)

# =====================================================
# RUN RETRIEVAL
# =====================================================

if st.button(
    "Run Retrieval",
    use_container_width=True
):

    with st.spinner(
        "Running Retrieval Pipeline..."
    ):

        pipeline = (
            RetrievalPipeline()
        )

        result = (
            pipeline.retrieve(
                query=query
            )
        )

    # =================================================
    # QUERY UNDERSTANDING
    # =================================================

    st.header(
        "🧠 Query Understanding"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "Intent"
        )

        st.write(
            result["intent"]
        )

    with col2:

        st.subheader(
            "Filters"
        )

        st.json(
            result["filters"]
        )

    # =================================================
    # RETRIEVAL METRICS
    # =================================================

    st.header(
        "📊 Retrieval Statistics"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Vector Results",
        result["num_vector_results"]
    )

    c2.metric(
        "Text Results",
        result["num_text_results"]
    )

    c3.metric(
        "Hybrid Results",
        result["num_hybrid_results"]
    )

    c4.metric(
        "Parent Docs",
        result["num_parent_documents"]
    )

    # =================================================
    # VECTOR RESULTS
    # =================================================

    st.header(
        "🔵 Vector Search Results"
    )

    for idx, chunk in enumerate(
        result["vector_results"],
        start=1
    ):

        with st.expander(
            f"{idx}. {chunk['_id']}"
        ):

            st.write(
                chunk["metadata"]
            )

            if "score" in chunk:

                st.write(
                    f"Score: {chunk['score']}"
                )

            st.text_area(
                "Chunk Text",
                chunk["chunk_text"],
                height=200,
                key=f"vector_{idx}"
            )

    # =================================================
    # TEXT RESULTS
    # =================================================

    st.header(
        "🟢 Text Search Results"
    )

    for idx, chunk in enumerate(
        result["text_results"],
        start=1
    ):

        with st.expander(
            f"{idx}. {chunk['_id']}"
        ):

            st.write(
                chunk["metadata"]
            )

            if "score" in chunk:

                st.write(
                    f"Score: {chunk['score']}"
                )

            st.text_area(
                "Chunk Text",
                chunk["chunk_text"],
                height=200,
                key=f"text_{idx}"
            )

    # =================================================
    # HYBRID RESULTS
    # =================================================

    st.header(
        "🟣 Hybrid Search Results"
    )

    for idx, chunk in enumerate(
        result["hybrid_results"],
        start=1
    ):

        with st.expander(
            f"{idx}. {chunk['_id']}"
        ):

            st.write(
                chunk["metadata"]
            )

            if "score" in chunk:

                st.write(
                    f"Score: {chunk['score']}"
                )

            st.text_area(
                "Chunk Text",
                chunk["chunk_text"],
                height=200,
                key=f"hybrid_{idx}"
            )

    # =================================================
    # RERANKED RESULTS
    # =================================================

    st.header(
        "⭐ Reranked Results"
    )

    for idx, chunk in enumerate(
        result["reranked_chunks"],
        start=1
    ):

        with st.expander(
            f"{idx}. {chunk['_id']}"
        ):

            st.write(
                chunk["metadata"]
            )

            if "score" in chunk:

                st.write(
                    f"Relevance Score: {chunk['score']}"
                )

            st.text_area(
                "Chunk Text",
                chunk["chunk_text"],
                height=200,
                key=f"rerank_{idx}"
            )

    # =================================================
    # PARENT DOCUMENTS
    # =================================================

    st.header(
        "📄 Parent Documents"
    )

    for idx, parent in enumerate(
        result["parent_documents"],
        start=1
    ):

        with st.expander(
            f"{idx}. {parent['_id']}"
        ):

            st.write(
                parent["metadata"]
            )

            if "match_count" in parent:

                st.write(
                    f"Match Count: {parent['match_count']}"
                )

            parent_text = (
                parent.get("text")
                or parent.get("content")
                or ""
            )

            st.text_area(
                "Parent Content",
                parent_text,
                height=300,
                key=f"parent_{idx}"
            )

    # =================================================
    # FINAL CONTEXT
    # =================================================

    st.header(
        "📚 Final Context Sent To LLM"
    )

    st.text_area(
        "Context",
        result["context"],
        height=600
    )