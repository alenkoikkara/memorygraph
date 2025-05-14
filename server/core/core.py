import datetime
from services.cohere import generate_keywords, generate_embedding
from utils.utils import prepare_embedding_text
from models.record import Record
from services.chromadb import add_document, semantic_search

def create_record(original: str, processed: str) -> Record:
    generated_json = generate_keywords(processed)
    embedding = generate_embedding(prepare_embedding_text(generated_json['summary'], generated_json['keywords']))
    # Determine content type
    content_type = 'url' if original.startswith(('http://', 'https://')) else 'text'

    record = Record(
        original_content=original,
        summary=generated_json['summary'],
        keywords=generated_json['keywords'],
        title=generated_json['title'],
        created_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        content_type=content_type,
        embedding=embedding,
        embedding_size=len(embedding)
    )
    
    add_document(embedding, record.title, record.summary, record.original_content, record.created_at, record.keywords)
    return record

def search_record(query: str, page: int = 1, page_size: int = 5):
    """
    Perform semantic search with pagination.
    
    Args:
        query: The search query string
        page: Page number (1-based)
        page_size: Number of results per page
        
    Returns:
        dict: {
            "matches": List of matching documents,
            "total": Total number of results,
            "page": Current page,
            "page_size": Results per page,
            "total_pages": Total number of pages
        }
    """
    embedding = generate_embedding(query)
    return semantic_search(embedding)