from arango import ArangoClient
import os
from dotenv import load_dotenv
from models.record import Record
# Load environment variables
load_dotenv()

# Get ArangoDB configuration from environment variables
ARANGO_HOST = os.getenv("ARANGO_HOST", "arangodb")  # Default to service name in Docker
ARANGO_PORT = os.getenv("ARANGO_PORT", "8529")
ARANGO_USER = os.getenv("ARANGO_USER", "root")
ARANGO_PASSWORD = os.getenv("ARANGO_PASSWORD", "root")
ARANGO_DB = os.getenv("ARANGO_DB", "_system")

# Initialize ArangoDB client and connect to database
client = ArangoClient(hosts=f"http://{ARANGO_HOST}:{ARANGO_PORT}")
db = client.db(ARANGO_DB, username=ARANGO_USER, password=ARANGO_PASSWORD)
graph = None

def initialize_database():
    """
    Initialize the database and ensure the collection exists.
    """
    global graph
    create_collection("summaries")
    graph = create_graph("memory_graph")

def create_collection(name: str):
    """
    Initialize the database and ensure the collection exists.
    
    Returns:
        Collection: The initialized collection
    """
    try:
        # Ensure the collection exists (create if not)
        if not db.has_collection("summaries"):
            db.create_collection("summaries")
        collection = db.collection("summaries")
        return collection
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
        raise
      
def create_graph(name: str):
    """
    Create a graph in the database.
    """
    try:
        graph = db.create_graph(name)
        return graph
    except Exception as e:  
        print(f"Error creating graph: {str(e)}")
        raise

def insert_documents_with_keywords(record: Record):
    """
    Insert a record into the database.
    
    Args:
        record: The record to insert
    """
    global graph
    if graph is None:
        raise Exception("Database not initialized. Call initialize_database() first.")
        
    # Ensure collections and edge definitions exist
    if not graph.has_vertex_collection('records'):
        graph.create_vertex_collection('records')
    if not graph.has_vertex_collection('keywords'):
        graph.create_vertex_collection('keywords')
    if not graph.has_edge_definition('recKeywords'):
        graph.create_edge_definition(
            edge_collection='recKeywords',
            from_vertex_collections=['records'],
            to_vertex_collections=['keywords']
        )
          
    # Get collection handles
    records_col = graph.vertex_collection('records')
    keywords_col = graph.vertex_collection('keywords')
    edges_col = graph.edge_collection('recKeywords')
      
    try:
        # Convert Record to dictionary for JSON serialization
        record_dict = record.model_dump()
        # Add a valid _key for the record
        record_dict['_key'] = record.created_at.replace(':', '-').replace('.', '-')
        records_col.insert(record_dict) 
    except Exception as e:
        print(f"Error inserting record: {str(e)}")
        raise
      
    # Process keywords
    for kw in record.keywords:
        # Create a valid ArangoDB key by removing invalid characters
        key = kw.strip().lower()
        key = ''.join(c for c in key if c.isalnum() or c in ['-', '_'])
        if not key:  # Skip empty keys
            continue
            
        try:
            keywords_col.insert({'_key': key, 'name': kw})
        except Exception as e:
            # Keyword already exists; nothing to do (or fetch if you need the doc)
            print(f"Error inserting keyword: {str(e)}")
            pass

        # Create the edge from document to keyword
        doc_id = f'records/{record_dict["_key"]}'
        kw_id = f'keywords/{key}'
        try:
            edges_col.insert({'_from': doc_id, '_to': kw_id})
        except Exception as e:
            # Edge already exists; skip
            print(f"Error inserting edge: {str(e)}")
            pass
