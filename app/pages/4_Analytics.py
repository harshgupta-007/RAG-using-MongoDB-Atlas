import sys
from pathlib import Path

ROOT_DIR = (
    Path(__file__)
    .resolve()
    .parents[2]
)

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import pandas as pd
import streamlit as st

from src.analytics.analytics_service import (
    AnalyticsService
)

analytics = (
    AnalyticsService()
)

st.title(
    "📈 Analytics Dashboard"
)

# ====================================
# Metrics
# ====================================

col1, col2 = st.columns(2)

col1.metric(
    "Total Searches",
    analytics.total_searches()
)

col2.metric(
    "Avg Retrieval Time (s)",
    analytics.avg_retrieval_time()
)

# ====================================
# Top Intents
# ====================================

st.header(
    "Top Intents"
)

intent_df = pd.DataFrame(
    analytics.top_intents()
)

if not intent_df.empty:

    intent_df.columns = [
        "Intent",
        "Count"
    ]

    st.bar_chart(
        intent_df.set_index(
            "Intent"
        )
    )

# ====================================
# Recent Searches
# ====================================

st.header(
    "Recent Searches"
)

recent_df = pd.DataFrame(
    analytics.recent_searches()
)

if not recent_df.empty:

    cols = [
        "query",
        "intent",
        "retrieval_time",
        "created_at"
    ]

    existing_cols = [
        c for c in cols
        if c in recent_df.columns
    ]

    st.dataframe(
        recent_df[
            existing_cols
        ]
    )