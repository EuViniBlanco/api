from typing import Optional
from pydantic import BaseModel

class Produto(BaseModel):
    id: Optional[str]
    nome: str
    descricao: str
    categoria: str