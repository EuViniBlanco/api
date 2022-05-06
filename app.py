from fastapi import FastAPI
from routes.app_route import app_route
from docs import tags_metadata

app = FastAPI()

app.include_router(app_route)