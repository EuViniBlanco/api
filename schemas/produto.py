def produtoEntity(item) -> dict: #Retorna um dicionario para o produto
    return {
        "id": str(item["_id"]),
        "nome": item["nome"],
        "descricao": item["descricao"],
        "categoria": item["categoria"]
    }

def produtosEntity(entity) -> list:
    return [produtoEntity(item) for item in entity]
