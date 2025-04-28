import time
import datetime
from services.cohere import generate_keywords
from pydantic import BaseModel

class Record(BaseModel):
    original_content: str
    summary: str
    keywords: list[str]
    title: str
    created_at: str
    content_type: str  # 'url' or 'text'

def create_record(original: str, processed: str) -> Record:
    generated_json = generate_keywords(processed)
    
    # Determine content type
    content_type = 'url' if original.startswith(('http://', 'https://')) else 'text'

    record = Record(
        original_content=original,
        summary=generated_json['summary'],
        keywords=generated_json['keywords'],
        title=generated_json['title'],
        created_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        content_type=content_type
    )
    return record
