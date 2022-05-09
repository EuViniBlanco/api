from fastapi import APIRouter, status, Response, HTTPException
from config.db import con
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


from models.categoria import Categoria
from schemas.categoria import categoriaEntity, categoriasEntity


from models.produto import Produto
from schemas.produto import produtoEntity, produtosEntity

app_route = APIRouter()

@app_route.get('/', tags=['Index'])
def root():
    return {"message": "Olá Irroba!"}

##  Rotas de Categoria  ##

@app_route.get('/categorias', response_model=list[Categoria], tags=['Categoria'])
def find_all_categorias():
        return categoriasEntity(con.local.categoria.find())

@app_route.post('/categoria', response_model=Categoria, tags=['Categoria'])
def create_categoria(categoria: Categoria):
    new_categoria = dict(categoria)
    del new_categoria["id"]
    id = con.local.categoria.insert_one(new_categoria).inserted_id
    return categoriaEntity(con.local.categoria.find_one({"_id": id}))

@app_route.get('/categoria/{id}', response_model=Categoria, tags=['Categoria'])
def find_categoria(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    else:
        return categoriaEntity(con.local.categoria.find_one({"_id": ObjectId(id)}))

@app_route.put('/categoria/{id}', response_model=Categoria, tags=['Categoria'])
def update_categoria(id: str, categoria: Categoria):
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    else:
        con.local.categoria.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": dict(categoria)})
        return categoriaEntity(con.local.categoria.find_one({"_id": ObjectId(id)}))

@app_route.delete('/categoria/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Categoria'])
def delete_categoria(id: str):
    if not con.local.categoria.find_one({"_id": ObjectId(id)}):
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    else:
        categoriaEntity(con.local.categoria.find_one_and_delete({"_id": ObjectId(id)}))
        return Response(status_code=HTTP_204_NO_CONTENT, content="Categoria deletada")


##  Rotas de Produto  ##

@app_route.get('/produtos', response_model=list[Produto], tags=['Produto'])
def find_all_produtos():
        return produtosEntity(con.local.produto.find())
    
@app_route.post('/produto', response_model=Produto, tags=['Produto'])
def create_produto(produto: Produto):
    new_produto = dict(produto, _id=ObjectId())
    del new_produto["id"] 
    #del new_produto["categoria"]
    id = con.local.produto.insert_one(new_produto).inserted_id
    return produtoEntity(con.local.produto.find_one({"_id": id}))

@app_route.get('/produto/{id}', response_model=Produto, tags=['Produto'])
def find_produto(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    else:
        return produtoEntity(con.local.produto.find_one({"_id": ObjectId(id)}))
    
@app_route.put('/produto/{id}', response_model=Produto, tags=['Produto'])
def update_produto(id: str, produto: Produto):
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    else:
        con.local.produto.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": dict(produto)})
        return produtoEntity(con.local.produto.find_one({"_id": ObjectId(id)}))
    
@app_route.delete('/produto/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Produto'])
def delete_produto(id: str):
    if not con.local.produto.find_one({"_id": ObjectId(id)}):
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    else:
        produtoEntity(con.local.produto.find_one_and_delete({"_id": ObjectId(id)}))
        return Response(status_code=HTTP_204_NO_CONTENT, content="Produto deletado")
