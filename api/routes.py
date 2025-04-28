from fastapi import APIRouter
from typing import Dict
from models.content import ContentInput
from models.record import Record
from services.record_service import RecordService

router = APIRouter()

@router.get("/", response_model=Dict[str, str])
async def read_root() -> Dict[str, str]:
    """Root endpoint returning a simple greeting."""
    return {"Hello": "World"}

@router.put("/api/v1/process", response_model=Record)
async def process_content(input: ContentInput) -> Record:
    """
    Process content (URL or text) and return a record with analysis.
    
    Args:
        input: ContentInput containing either URL or text content
        
    Returns:
        Record: Processed record containing summary, keywords, and metadata
    """
    original, content = input.get_content()
    return RecordService.create_record(original, content) 