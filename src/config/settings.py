from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MONGO_URI: str

    DATABASE_NAME: str

    PARENT_COLLECTION: str

    CHILD_COLLECTION: str

    VECTOR_INDEX_NAME: str

    VOYAGE_API_KEY: str

    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()