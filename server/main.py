from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from services.arangodb import initialize_database
from services.chromadb import initialize_chroma
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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
    
    # Configure CORS
    allowed_origins = [
        "http://localhost:3000",  # Local development
        "http://localhost:8000",  # Local development alternative
        "http://localhost:5173",  # Local development alternative
        "http://localhost",  # Local development alternative
        "https://memorygraph.alenkoikkara.com",  # Production domain
        "https://www.memorygraph.alenkoikkara.com",  # Production domain with www
        "chrome-extension://fmlccacimliaejecjkkhegmfmhgnfkok"  # Specific Chrome extension ID
    ]
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
        expose_headers=["*"],
        max_age=600,  # Cache preflight requests for 10 minutes
    )
    
    # Initialize database
    initialize_chroma()
    initialize_database()
    # Include API router
    app.include_router(router)
    
    return app

app = create_app()

