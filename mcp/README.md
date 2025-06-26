# Simple Books MCP Server (FastAPI)

This is a Model-Connected Platform (MCP) server for the Simple Books API, implemented in Python using FastAPI.

## Setup

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

```bash
uvicorn main:app --reload
```

- The API will be available at `http://localhost:8000`.
- Interactive docs: `http://localhost:8000/docs`

## Exposing the Server with ngrok

To make your local MCP server accessible over the internet (for testing or integration), you can use [ngrok](https://ngrok.com/):

1. **Start the FastAPI server** (from the project root):
   ```bash
   uvicorn mcp.main:app --reload
   ```
   The server will run at `http://localhost:8000` by default.

2. **Expose your local server with ngrok:**
   ```bash
   ngrok http 8000
   ```
   This will provide a public URL (e.g., `https://xxxx-xxx-xxx-xxx.ngrok-free.app`) that forwards to your local server.

3. **Update your configuration:**
   - Use the ngrok URL as the base URL for your MCP server in any client or integration (e.g., in `mcp.json`).

**Notes:**
- You need to have ngrok installed. [Download ngrok here.](https://ngrok.com/download)
- The free version of ngrok generates a new URL each time you start it. For a persistent URL, consider signing up for an ngrok account and using reserved domains.
- Make sure your firewall allows incoming connections to the port you are exposing (default: 8000).

## Endpoints
- `POST /api-clients` — Register a new API client (get JWT access token)
- `GET /books` — List books (optionally filter by type)
- `GET /books/{bookId}` — Get details of a specific book
- `GET /orders` — List all orders (requires Bearer JWT)
- `POST /orders` — Create a new order (requires Bearer JWT)
- `GET /orders/{orderId}` — Get details of a specific order (requires Bearer JWT)
- `GET /status` — Health check

## Notes
- This server uses in-memory storage for demo purposes.
- JWT secret is hardcoded for demo; use environment variables in production. 

## Setting up MCP on Cursor

To work with this MCP server in [Cursor](https://www.cursor.so/):

1. **Open the project in Cursor:**
   - Launch Cursor and open the root directory of this repository.

2. **Configure MCP servers:**
   - Edit the `.cursor/mcp.json` file in the project root to add or update your MCP server configuration. Example:
     ```json
     {
       "mcpServers": {
         "simplebooks-local": {
           "url": "http://localhost:8000",
           "description": "Local Simple Books MCP server"
         }
       }
     }
     ```
   - For remote access (e.g., via ngrok), use your public ngrok URL as the value for `url`.

3. **Use the Cursor terminal:**
   - You can run, test, and debug the MCP server directly from the integrated terminal in Cursor.
   - All API endpoints and development workflows are available as described below.

4. **Leverage Cursor features:**
   - Use Cursor's AI, code navigation, and search tools to explore and extend the MCP server codebase efficiently.

