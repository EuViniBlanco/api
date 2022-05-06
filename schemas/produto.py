def produtoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "nome": item["nome"],
        "descricao": item["descricao"],
        "preco": item["preco"],
    }

def produtosEntity(entity) -> list:
    return [produtoEntity(item) for item in entity]