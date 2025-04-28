from pydantic import BaseModel
from typing import List
from datetime import datetime

class Record(BaseModel):
    """Model representing a processed content record."""
    original_content: str
    summary: str
    keywords: List[str]
    title: str
    created_at: str
    content_type: str  # 'url' or 'text'

    class Config:
        """Pydantic model configuration."""
        json_schema_extra = {
            "example": {
                "original_content": "https://example.com",
                "summary": "Example summary",
                "keywords": ["example", "test"],
                "title": "Example Title",
                "created_at": datetime.now().isoformat(),
                "content_type": "url"
            }
        } 