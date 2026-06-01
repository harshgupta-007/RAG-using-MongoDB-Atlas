from src.database.collections import (
    child_collection
)

docs = child_collection.find(
    {},
    {
        "metadata.chapter": 1
    }
)

chapters = set()

for doc in docs:

    chapter = (
        doc.get("metadata", {})
        .get("chapter")
    )

    if chapter:
        chapters.add(chapter)

for chapter in sorted(chapters):

    print(repr(chapter))