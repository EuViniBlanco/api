from fastapi import APIRouter
from config.db import con
from models.categoria import Categoria
from schemas.categoria import categoriaEntity, categoriasEntity
from models.categoria import Categoria

categoria = APIRouter()

@categoria.get('/categoria')
def find_all_categoria():
    return categoriasEntity(con.local.categoria.find())

@categoria.post('/categoria')
def create_categoria(categoria: Categoria):
    new_categoria = dict(categoria)
    print(new_categoria)
    return "received"

@categoria.get('/categoria/{id}')
def find_categoria():
    return "Hello World"

@categoria.put('/categoria/{id}')
def update_categoria():
    return "Hello World"

@categoria.delete('/categoria/{id}')
def delete_categoria():
    return "Hello World"