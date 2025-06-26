from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp.routes import router

app = FastAPI(title="Simple Books MCP API", description="API for managing books and orders", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/status")
def get_status():
    return {"status": "OK"} 