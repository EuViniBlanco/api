from typing import Optional
from pydantic import BaseModel, Field
from models.categoria import Categoria
from schemas.categoria import categoriaEntity

class Produto(BaseModel):
    id: Optional[str]
    nome: str
    descricao: str
    categoria: str