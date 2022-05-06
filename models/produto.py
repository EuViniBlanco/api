from typing import Optional
from pydantic import BaseModel
from models.categoria import Categoria

class Produto(BaseModel):
    id: Optional[str]
    nome: str
    descricao: str
    preco: float
    categoria: Categoria
    
class Config:
    orm_mode = True

def __repr__(self):
    return f"Produto(id={self.id}, nome={self.nome}, descricao={self.descricao}, preco={self.preco}, categoria={self.categoria})"