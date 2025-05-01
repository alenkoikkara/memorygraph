from typing import List

def prepare_embedding_text(summary: str, keywords: List[str]) -> str:
    keywords_text = ", ".join(keywords)
    return f"{summary}\nKeywords: {keywords_text}"
