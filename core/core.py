import datetime
from services.cohere import generate_keywords, generate_embedding
from utils.utils import prepare_embedding_text
from models.record import Record
from services.arangodb import insert_documents_with_keywords

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
    insert_documents_with_keywords(record)
    return record
