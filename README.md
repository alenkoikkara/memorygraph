# FastAPI Content Processing Application

A FastAPI-based application that processes content, supporting both URL and text input. The application can extract main content from URLs or process direct text input.

## Features

- URL content extraction
- Text content processing
- RESTful API endpoints
- Docker containerization support

## Prerequisites

- Python 3.11 or higher
- Docker and Docker Compose
- pip (Python package manager)

## Installation

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Build and run using Docker Compose:
```bash
docker-compose up --build
```

The application will be available at `http://localhost:8000`

### Manual Installation

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn main:app --reload
```

## API Endpoints

### GET /
- Description: Health check endpoint
- Response: `{"Hello": "World"}`

### PUT /api/v1/process
- Description: Process content (URL or text)
- Request Body:
```json
{
    "content": "https://example.com"  // or any text content
}
```
- Response: Processed record with extracted content

## Development

The project structure:
```
.
├── core/           # Core application logic
├── services/       # Service implementations
├── database/       # Database related files
├── main.py         # Application entry point
├── requirements.txt # Project dependencies
└── Dockerfile      # Container configuration
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 