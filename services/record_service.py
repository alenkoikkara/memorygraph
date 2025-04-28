from datetime import datetime
from typing import Dict, Any
from models.record import Record
from services.cohere import generate_keywords

class RecordService:
    """Service class for handling record creation and management."""
    
    @staticmethod
    def create_record(original: str, processed: str) -> Record:
        """
        Create a new record from original and processed content.
        
        Args:
            original: The original content (URL or text)
            processed: The processed content (extracted text or full text)
            
        Returns:
            Record: A new record instance
        """
        generated_data: Dict[str, Any] = generate_keywords(processed)
        
        # Determine content type
        content_type = 'url' if original.startswith(('http://', 'https://')) else 'text'

        return Record(
            original_content=original,
            summary=generated_data['summary'],
            keywords=generated_data['keywords'],
            title=generated_data['title'],
            created_at=datetime.now(datetime.timezone.utc).isoformat(),
            content_type=content_type
        ) 