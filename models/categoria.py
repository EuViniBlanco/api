from typing import Optional
from pydantic import BaseModel

class Categoria(BaseModel):
    id: Optional[str]
    nome: str
    descricao: str