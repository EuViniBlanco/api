from typing import Optional
from pydantic import BaseModel
#from models.produto import Produto

class Categoria(BaseModel):
    id: Optional[str]
    nome: str
    descricao: str
    