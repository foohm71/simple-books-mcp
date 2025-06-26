# Simple Books API (Backend)

This repository contains the backend API for the Simple Books project, implemented with FastAPI. It provides endpoints for listing books, placing orders, and managing clients.

## Features
- List available books
- Place and view orders
- Register API clients and obtain access tokens
- JWT-based authentication for order endpoints

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd simple-books-mcp
   ```

2. **Set up the backend environment:**
   ```bash
   cd mcp
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the API server:**
   From the project root:
   ```bash
   uvicorn mcp.main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

## API Endpoints
- `POST /api-clients` — Register a new API client (get JWT access token)
- `GET /books` — List books (optionally filter by type)
- `GET /books/{bookId}` — Get details of a specific book
- `GET /orders` — List all orders (requires Bearer JWT)
- `POST /orders` — Create a new order (requires Bearer JWT)
- `GET /orders/{orderId}` — Get details of a specific order (requires Bearer JWT)
- `GET /status` — Health check

## API Documentation
API documentation and specifications are located in the `api/` directory:
- `api/swagger.yaml` — OpenAPI/Swagger specification
- `api/Simple Books API.postman_collection.json` — Postman collection
- `api/index.html` — Swagger UI viewer

### Viewing the API Documentation
- **Swagger UI:**
  1. Navigate to the `api` directory:
     ```bash
     cd api
     python3 -m http.server 8000
     ```
  2. Open your browser and visit: http://localhost:8000
- **Swagger Editor Online:**
  1. Go to https://editor.swagger.io/
  2. Copy the contents of `api/swagger.yaml` and paste into the editor.
- **Postman:**
  1. Import `api/Simple Books API.postman_collection.json` into Postman.

## Notes
- This server uses in-memory storage for demo purposes.
- JWT secret is hardcoded for demo; use environment variables in production.
- For public access or integration, you can expose your local server using ngrok. See `mcp/README.md` for details.

## Deployment with ngrok

For instructions on how to expose your local API server to the internet using ngrok, see the [mcp/README.md](mcp/README.md) file. 