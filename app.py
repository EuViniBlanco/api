from fastapi import FastAPI
from routes.app_route import app_route
from docs import tags_metadata

app = FastAPI(
    title="FastAPI - Irroba",
    description="FastAPI - Python, MongoDB e Docker",
    version="0.0.1",
)

app.include_router(app_route, prefix="/api/v1")