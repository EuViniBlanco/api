def categoriaEntity(item) -> dict:
    return {
        "id": item["id"],
        "nome": item["nome"],
        "descricao": item["descricao"]
    }

def categoriasEntity(entity) -> list:
    [categoriaEntity(item) for item in entity]