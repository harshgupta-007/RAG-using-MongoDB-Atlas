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

st.set_page_config(
    page_title="MongoDB Atlas RAG",
    page_icon="🤖",
    layout="wide"
)

from src.chat.chat_service import (
    ChatService
)

from src.pipelines.rag_pipeline import (
    RAGPipeline
)
from src.utils.logger import (
    logger
)

# =====================================================
# INITIALIZATION
# =====================================================

chat_service = ChatService()

if "pipeline" not in st.session_state:

    st.session_state.pipeline = (
        RAGPipeline()
    )

# =====================================================
# SIDEBAR
# =====================================================

# st.sidebar.title("Chats")

sessions = (
    chat_service
    .get_all_sessions()
)
st.sidebar.title(
    "🗂️ Chat Sessions"
)

st.sidebar.caption(
    f"{len(sessions)} Sessions"
)
# =====================================================
# NEW CHAT
# =====================================================

if st.sidebar.button(
    "+ New Chat",
    use_container_width=True
):

    session_id = (
        chat_service
        .create_new_chat()
    )

    st.session_state[
        "session_id"
    ] = session_id

    st.rerun()

# =====================================================
# DEFAULT CHAT
# =====================================================

if "session_id" not in st.session_state:

    if sessions:

        st.session_state[
            "session_id"
        ] = sessions[0]["_id"]

# =====================================================
# SESSION LIST
# =====================================================

st.sidebar.markdown("---")

for session in sessions:

    if st.sidebar.button(
        session["title"],
        key=session["_id"],
        use_container_width=True
    ):

        st.session_state[
            "session_id"
        ] = session["_id"]

        st.rerun()

# =====================================================
# MAIN CHAT WINDOW
# =====================================================

st.title(
    "🤖 MongoDB Atlas RAG Assistant"
)

st.caption(
    "Hybrid Search • Voyage Reranker • Gemini • MongoDB Atlas"
)

# =====================================================
# LOAD CHAT HISTORY
# =====================================================

messages = (
    chat_service
    .load_chat(
        st.session_state[
            "session_id"
        ]
    )
)

# =====================================================
# DISPLAY CHAT HISTORY
# =====================================================

for message in messages:

    # with st.chat_message(
    #     message["role"]
    # ):
    with st.chat_message(
        message["role"],
        avatar="👤"
        if message["role"] == "user"
        else "🤖"
    ):

        st.markdown(
            message["content"]
        )

        if (
            message["role"]
            == "assistant"
        ):

            metadata = (
                message.get(
                    "metadata",
                    {}
                )
            )

            if metadata:

                # with st.expander(
                #     "Intent"
                # ):
                with st.expander(
                    "🧠 Query Understanding",
                    expanded=False
                ):

                    st.write(
                        metadata.get(
                            "intent"
                        )
                    )

                # with st.expander(
                #     "Filters"
                # ):
                    
                with st.expander(
                    "📋 Metadata Filters",
                    expanded=False
                ):

                    st.json(
                        metadata.get(
                            "filters",
                            {}
                        )
                    )

                # with st.expander(
                #     "Sources"
                # ):
                with st.expander(
                    "📚 Retrieved Sources",
                    expanded=False
                ):

                    st.write(
                        metadata.get(
                            "sources",
                            []
                        )
                    )

# =====================================================
# CHAT INPUT
# =====================================================

prompt = st.chat_input(
    "Ask a question..."
)

# =====================================================
# NEW QUESTION
# =====================================================

if prompt:

    # -----------------------------------------
    # Save User Message
    # -----------------------------------------

    chat_service.history.save_message(
        session_id=
            st.session_state[
                "session_id"
            ],

        role="user",

        content=prompt
    )


    messages = (
        chat_service.load_chat(
            st.session_state[
                "session_id"
            ]
        )
    )

    if len(messages) == 1:

        chat_service.auto_title(
            st.session_state[
                "session_id"
            ],
            prompt
        )

    with st.chat_message(
        "user"
    ):

        st.markdown(
            prompt
        )

    # -----------------------------------------
    # RAG
    # -----------------------------------------

    with st.spinner(
        "Thinking..."
    ):
        try:
    

            result = (
                st.session_state
                .pipeline
                .ask(
                    prompt
                )
            )
        except Exception as e:

            logger.exception(
                "Chat Request Failed"
            )

            st.error(
                "⚠️ Unable to process your request."
            )

            st.stop()

    answer = result["answer"]

    # -----------------------------------------
    # Assistant Response
    # -----------------------------------------

    with st.chat_message(
        "assistant"
    ):

        st.markdown(
            answer
        )

        with st.expander(
            "Intent"
        ):

            st.write(
                result["intent"]
            )

        with st.expander(
            "Filters"
        ):

            st.json(
                result["filters"]
            )

        with st.expander(
            "Sources"
        ):

            for source in result[
                "sources"
            ]:

                st.write(
                    source["_id"]
                )

                # st.write(
                #     source["metadata"]
                # )
                st.json(
                    source["metadata"]
                )

    # -----------------------------------------
    # Save Assistant Message
    # -----------------------------------------

    chat_service.history.save_message(
        session_id=
            st.session_state[
                "session_id"
            ],

        role="assistant",

        content=answer,

        metadata={

            "intent":
                str(
                    result["intent"]
                ),

            "filters":
                result["filters"],

            "sources":
                [
                    source["_id"]

                    for source in result[
                        "sources"
                    ]
                ]
        }
    )

    # -----------------------------------------
    # Update Session Timestamp
    # -----------------------------------------

    chat_service.history.update_session_timestamp(
        st.session_state[
            "session_id"
        ]
    )

    st.rerun()