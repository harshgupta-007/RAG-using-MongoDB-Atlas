from typing import Optional
from pydantic import BaseModel


class QueryIntent(BaseModel):

    intent: str = "find"

    chapter: Optional[str] = None

    section: Optional[str] = None

    page_start: Optional[int] = None

    page_end: Optional[int] = None

    search_query: Optional[str] = None