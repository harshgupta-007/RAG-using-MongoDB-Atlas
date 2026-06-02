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

from src.database.collections import (
    db,
    parent_collection,
    child_collection
)

from src.config.settings import (
    settings
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="System Info",
    page_icon="⚙️",
    layout="wide"
)

st.title(
    "⚙️ System Information"
)

# =====================================================
# DATABASE STATUS
# =====================================================

st.header(
    "🗄️ MongoDB"
)

try:

    db.command(
        "ping"
    )

    st.success(
        "MongoDB Connection Successful"
    )

except Exception as e:

    st.error(
        f"MongoDB Error: {e}"
    )

# =====================================================
# COLLECTION COUNTS
# =====================================================

st.header(
    "📊 Collection Statistics"
)

parent_count = (
    parent_collection.count_documents({})
)

child_count = (
    child_collection.count_documents({})
)

chat_sessions_count = (
    db["chat_sessions"]
    .count_documents({})
)

chat_messages_count = (
    db["chat_messages"]
    .count_documents({})
)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Parent Documents",
    parent_count
)

c2.metric(
    "Child Chunks",
    child_count
)

c3.metric(
    "Chat Sessions",
    chat_sessions_count
)

c4.metric(
    "Chat Messages",
    chat_messages_count
)

# =====================================================
# MODEL INFORMATION
# =====================================================

st.header(
    "🤖 Models"
)

model_info = {

    "Embedding Model":
        "voyage-3-large",

    "Reranker Model":
        "rerank-2",

    "LLM":
        "gemini-2.5-flash"
}

st.json(
    model_info
)

# =====================================================
# CONFIGURATION
# =====================================================

st.header(
    "⚙️ Configuration"
)

config_info = {

    "Database":
        settings.DATABASE_NAME,

    "Parent Collection":
        settings.PARENT_COLLECTION,

    "Child Collection":
        settings.CHILD_COLLECTION,

    "Embedded Collection":
        settings.CHILD_COLLECTION
}

st.json(
    config_info
)

# =====================================================
# INDEX INFORMATION
# =====================================================

st.header(
    "🔎 Search Indexes"
)

index_info = {

    "Vector Index":
        "vector_index",

    "Text Index":
        "text_index"
}

st.json(
    index_info
)

# =====================================================
# ENVIRONMENT
# =====================================================

st.header(
    "🐍 Environment"
)

st.write(
    sys.executable
)

st.write(
    sys.version
)