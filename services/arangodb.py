from arango import ArangoClient
import os
from dotenv import load_dotenv

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

def initialize_database():
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

def insert_record(record):
    """
    Insert a record into the database.
    
    Args:
        record: The record to insert
    """
    try:
        collection = initialize_database()
        collection.insert(record)
    except Exception as e:
        print(f"Error inserting record: {str(e)}")
        raise
