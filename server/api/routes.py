from fastapi import APIRouter, Query
from typing import Dict, List, Any
from models.content import ContentInput, SearchQuery
from core.core import Record, create_record, search_record

router = APIRouter()

@router.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint that returns a simple greeting."""
    return {"message": "Welcome to Memory Graph API"}

@router.put("/api/process")
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

@router.get("/api/search")
async def search(
    query: str = Query(..., description="The search query to find relevant documents"),
    page: int = Query(1, description="Page number (1-based)"),
    page_size: int = Query(5, description="Number of results per page")
):
    """
    Perform semantic search on the content database with pagination.

    Args:
        query: The search query string (passed as URL parameter)
        page: Page number (1-based)
        page_size: Number of results per page
        
    Returns:
        Dict[str, Any]: {
            "matches": List of matching documents,
            "total": Total number of results,
            "page": Current page,
            "page_size": Results per page,
            "total_pages": Total number of pages
        }
    """
    return search_record(query, page, page_size)