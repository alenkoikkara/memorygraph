# Memento

A full-stack application for processing, storing, and searching content with semantic search capabilities. The application consists of a FastAPI backend, React frontend, Chrome extension, and uses ChromaDB for vector storage.

## Features

- **Content Processing**
  - URL content extraction with intelligent text parsing
  - Direct text input processing
  - Automatic content summarization and keyword extraction using Cohere AI

- **Semantic Search**
  - Vector-based semantic search using ChromaDB
  - Real-time search results
  - Efficient content retrieval

- **Chrome Extension**
  - One-click URL saving
  - Seamless integration with the backend API
  - User-friendly popup interface

- **Modern Web Interface**
  - Responsive design with Tailwind CSS
  - Client-side routing with React Router
  - Real-time search functionality
  - Clean and intuitive user interface

## Architecture

The application is built using a microservices architecture with the following components:

- **Backend (FastAPI)**
  - RESTful API endpoints
  - Content processing and storage
  - Semantic search functionality
  - CORS support for cross-origin requests
  - Cohere AI integration for content analysis

- **Frontend (React)**
  - Modern UI with Tailwind CSS
  - Client-side routing
  - Responsive design
  - API integration
  - Environment-based configuration

- **Chrome Extension**
  - Browser integration
  - URL saving functionality
  - User-friendly interface
  - Secure API communication

- **Database**
  - ChromaDB for vector storage and semantic search
  - Persistent storage with Docker volumes

## Prerequisites

- Docker and Docker Compose
- Node.js 20 or higher
- Python 3.11 or higher
- Chrome browser (for extension)
- Cohere AI API key

## Environment Variables

### Backend (.env)
```
COHERE_API_KEY=your_cohere_api_key
CHROMA_HOST=chromadb
CHROMA_PORT=8000
```

### Frontend (.env)
```
VITE_BACKEND_BASE_URL=http://localhost:8001/api
```

## Installation

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Set up environment variables:
   - Create `.env` file in the server directory with required variables
   - Create `.env` file in the ui directory with required variables

3. Build and run using Docker Compose:
```bash
docker-compose up --build
```

The application will be available at:
- Frontend: `http://localhost`
- Backend API: `http://localhost/api`
- API Documentation: `http://localhost/docs`

### Manual Installation

#### Backend

1. Create a virtual environment:
```bash
cd server
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run the application:
```bash
uvicorn main:app --reload
```

#### Frontend

1. Install dependencies:
```bash
cd ui
npm install
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Run the development server:
```bash
npm run dev
```

#### Chrome Extension

1. Open Chrome and navigate to `chrome://extensions/`
2. Enable "Developer mode"
3. Click "Load unpacked" and select the `chrome-extension` directory

## API Endpoints

### Content Processing
- `PUT /api/process`
  - Process content (URL or text)
  - Request Body:
  ```json
  {
      "content": "https://example.com"  // or any text content
  }
  ```

### Search
- `GET /api/search`
  - Search content with semantic search
  - Query Parameters:
    - `query`: Search query string

## Project Structure

```
.
├── server/           # FastAPI backend
│   ├── api/         # API routes and endpoints
│   ├── core/        # Core application logic
│   ├── services/    # Service implementations
│   └── models/      # Data models
├── ui/              # React frontend
│   ├── src/         # Source code
│   ├── public/      # Static assets
│   └── dist/        # Build output
├── chrome-extension/ # Chrome extension
│   ├── popup.html   # Extension popup
│   ├── popup.js     # Extension logic
│   └── manifest.json # Extension configuration
├── nginx/           # Nginx configuration
└── docker-compose.yml # Docker configuration
```

## Development Workflow

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit them:
```bash
git add .
git commit -m "Description of your changes"
```

3. Push your branch and create a Pull Request:
```bash
git push origin feature/your-feature-name
```

4. The CI/CD pipeline will automatically:
   - Build and test your changes
   - Create Docker images
   - Deploy to staging (if configured)

