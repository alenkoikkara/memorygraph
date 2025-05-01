from fastapi import FastAPI
from api.routes import router
from services.arangodb import initialize_database
from services.chromadb import initialize_chroma
def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    
    Returns:
        FastAPI: Configured FastAPI application instance
    """
    app = FastAPI(
        title="Memory Graph API",
        description="API for processing and storing content summaries",
        version="1.0.0"
    )
    
    # Initialize database
    initialize_chroma()
    initialize_database()
    # Include API router
    app.include_router(router)
    
    return app

app = create_app()

