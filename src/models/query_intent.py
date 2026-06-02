from pydantic import BaseModel
from typing import Optional


class QueryIntent(BaseModel):

    intent: str = "find"

    chapter: str | None = None

    section: str | None = None

    page_start: int | None = None

    page_end: int | None = None

    search_query: str = ""