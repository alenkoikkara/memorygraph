from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Record(BaseModel):
    """Model representing a processed content record."""
    original_content: str
    summary: str
    keywords: List[str]
    title: str
    created_at: str
    content_type: str  # 'url' or 'text'
    embedding_size: Optional[int] = None
    embedding: Optional[list[float]] = None

    class Config:
        """Pydantic model configuration."""
        json_schema_extra = {
            "example": {
                "original_content": "https://example.com",
                "summary": "Example summary",
                "keywords": ["example", "test"],
                "title": "Example Title",
                "created_at": datetime.now().isoformat(),
                "content_type": "url",
                "embedding_size": 3,
                "embedding": [0.1, 0.2, 0.3]
            }
        } 