from fastapi import FastAPI
from routes.app_route import app_route
from docs import tags_metadata as tags #Importação de tags para o swagger (docs), para o fastapi (tags) e para o uvicorn (tags)

app = FastAPI(
    title="FastAPI - Irroba",
    description="FastAPI - Python, MongoDB e Docker",
    version="0.0.1",
)

app.include_router(app_route, prefix="/api/v1") #Incluir o router na aplicação (prefixo /api/v1) para que seja possível acessar as rotas da aplicação