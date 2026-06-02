from src.chat.chat_history import (
    ChatHistory
)
from src.generation.chat_title_generator import (
    ChatTitleGenerator
)

class ChatService:

    def __init__(self):

        self.history = (
            ChatHistory()
        )
        self.title_generator = (
            ChatTitleGenerator()
        )

    def create_new_chat(self):

        return (
            self.history.create_session(
                "New Chat"
            )
        )

    def get_all_sessions(self):

        return (
            self.history.get_sessions()
        )

    def load_chat(
        self,
        session_id
    ):

        return (
            self.history.get_messages(
                session_id
            )
        )
    
    def auto_title(
        self,
        session_id,
        first_message
    ):

        title = (
            self.title_generator.generate(
                first_message
            )
        )

        self.history.update_title(
            session_id,
            title
        )