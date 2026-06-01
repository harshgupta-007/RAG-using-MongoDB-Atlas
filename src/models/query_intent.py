from pydantic import BaseModel
from typing import Optional


class QueryIntent(BaseModel):

    intent: str

    chapter: Optional[str] = None

    section: Optional[str] = None

    page_start: Optional[int] = None

    page_end: Optional[int] = None

    search_query: str