from src.chat.chat_history import (
    ChatHistory
)

chat = ChatHistory()

session_id = (
    chat.create_session(
        "Test Session"
    )
)

print(session_id)

chat.save_message(
    session_id,
    "user",
    "Hello"
)

chat.save_message(
    session_id,
    "assistant",
    "Hi there"
)

messages = (
    chat.get_messages(
        session_id
    )
)

for msg in messages:

    print(
        msg["role"],
        msg["content"]
    )