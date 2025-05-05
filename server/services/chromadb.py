from arango import ArangoClient
import os
from dotenv import load_dotenv
from models.record import Record
import chromadb
from datetime import datetime
# Load environment variables
load_dotenv()

# Get ArangoDB configuration from environment variables
CHROMA_HOST = os.getenv("CHROMA_HOST", "chromadb")  # Default to service name in Docker
CHROMA_PORT = os.getenv("CHROMA_PORT", "8000") # Convert to integer

chroma_client = chromadb.HttpClient(host=CHROMA_HOST, port=int(CHROMA_PORT))
chroma_client.heartbeat()
collection = None

def initialize_chroma():
    """
    Initialize the database and ensure the collection exists.
    """
    global collection
    collection = chroma_client.get_or_create_collection(name="documents")
    print("Chroma initialized")
    return collection


def add_document(embedding, title, summary, content, created_at, tags):
    # Combine summary and tags for embedding text

    # Use title (or any unique string) as the document ID
    doc_id = title.lower().replace(" ", "_")
    # Add the document, its embedding, and metadata to ChromaDB
    collection.add(
        ids=[doc_id],
        documents=[content],
        embeddings=[embedding],
        metadatas=[{
            "title": title,
            "created_at": created_at,
            "summary": summary
        }]
    )
    
def semantic_search(embedding, page=1, page_size=5):
    """
    Perform semantic search with pagination.
    
    Args:
        embedding: The embedding vector to search with
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
    # Get total count first
    total = collection.count()
    
    # Calculate the range of results we need
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    
    # Query ChromaDB for all results (we'll paginate them ourselves)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=total  # Get all results
    )
    
    # Collect and return matching documents with metadata and distance
    matches = []
    for doc, metadata, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
    ):
        matches.append({
            "url": doc,
            "title": metadata.get("title"),
            "created_at": datetime.fromisoformat(metadata.get("created_at")).strftime("%Y-%m-%d %H:%M:%S"),
            "tags": metadata.get("tags"),
            "summary": metadata.get("summary"),
            "distance": dist
        })
    
    # Results are sorted by increasing distance (i.e. most similar first)
    matches.sort(key=lambda x: x["distance"])
    
    # Apply pagination by slicing the results
    paginated_matches = matches[start_idx:end_idx]
    
    return {
        "matches": paginated_matches,
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": (total + page_size - 1) // page_size  # Ceiling division
    }

