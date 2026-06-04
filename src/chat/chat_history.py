from datetime import datetime
import uuid

from src.database.collections import (
    db
)

from src.utils.logger import (
    logger
)

class ChatHistory:

    def __init__(self):

        self.sessions = (
            db["chat_sessions"]
        )

        self.messages = (
            db["chat_messages"]
        )

    def create_session(
        self,
        title="New Chat"
    ):

        session_id = (
            str(uuid.uuid4())
        )

        self.sessions.insert_one(
            {
                "_id": session_id,

                "title": title,

                "created_at":
                    datetime.utcnow(),

                "updated_at":
                    datetime.utcnow()
            }
        )
        logger.info(
            f"Session Created: {session_id}"
        )

        return session_id
    

    def save_message(
        self,
        session_id,
        role,
        content,
        metadata=None
    ):

        self.messages.insert_one(
            {
                "_id":
                    str(uuid.uuid4()),

                "session_id":
                    session_id,

                "role":
                    role,

                "content":
                    content,

                "metadata":
                    metadata or {},

                "created_at":
                    datetime.utcnow()
            }
        )
        logger.info(
            f"Message Saved | "
            f"Role={role}"
        )

    def get_messages(
        self,
        session_id
    ):

        return list(

            self.messages.find(
                {
                    "session_id":
                        session_id
                }
            ).sort(
                "created_at",
                1
            )

        )
    

    def get_sessions(self):

        return list(

            self.sessions.find()

            .sort(
                "updated_at",
                -1
            )

        )
    

    def update_session_timestamp(
        self,
        session_id
    ):

        self.sessions.update_one(
            {
                "_id": session_id
            },
            {
                "$set": {
                    "updated_at":
                        datetime.utcnow()
                }
            }
        )


    def update_title(
        self,
        session_id,
        title
    ):

        self.sessions.update_one(
            {
                "_id": session_id
            },
            {
                "$set": {
                    "title": title
                }
            }
        )