from fastapi import APIRouter, Query
from typing import Dict, List, Any
from models.content import ContentInput, SearchQuery
from core.core import Record, create_record, search_record

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

@router.get("/search")
async def search(
    query: str = Query(..., description="The search query to find relevant documents")
):
    """
    Perform semantic search on the content database.

    Args:
        query: The search query string (passed as URL parameter)
        
    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing search results
    """
    return search_record(query)