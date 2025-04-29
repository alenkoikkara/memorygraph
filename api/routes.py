from fastapi import APIRouter
from typing import Dict
from models.content import ContentInput
from core.core import Record, create_record

router = APIRouter()

@router.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint that returns a simple greeting."""
    return {"message": "Welcome to Memory Graph API"}

@router.put("/process")
async def process_content(content: ContentInput) -> Record:
    """
    Process content and return a record with summary, keywords, and title.
    
    Args:
        content: ContentInput object containing either URL or text content
        
    Returns:
        Record: Processed record containing summary, keywords, and title
    """
    processed_content = content.get_content()
    return create_record(content.content, processed_content) 