def categoriaEntity(item) -> dict:  #Retorna um dicionario
    return {
        "id": str(item["_id"]),
        "nome": item["nome"],
        "descricao": item["descricao"],
    }

def categoriasEntity(entity) -> list: 
    return [categoriaEntity(item) for item in entity] 