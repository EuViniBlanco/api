# FastAPI - Python, MongoDB e Docker

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%40viniciusblanco-blue)](https://www.linkedin.com/in/viniciusblanco/)

Versões utilizadas no projeto [aqui](https://github.com/EuViniBlanco/api/blob/main/requirements.txt)
### Instalando FastAPI
```
pip install "fastapi"
```

You can also install it part by part.

This is what you would probably do once you want to deploy your application to production:

```
pip install fastapi
```
Also install uvicorn to work as the server:


```
pip install "uvicorn"
```

## what is uvicorn ?
Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

## What is pydentic model
You can think of models as similar to types in strictly typed languages, or as the requirements of a single endpoint in an API.

## Iniciar server 
```
uvicorn app:app --port 8086 --reload
```

## Acessar a API via FastAPI
http://localhost:8086/

Para acessar o teste da API, basta acessar `/docs`:

http://localhost:8086/docs



# Estrutura do Projeto:
## models:
[Todos arquivos de models aqui](https://github.com/EuViniBlanco/api/tree/main/models)

## schemas:
[Todos arquivos de Schemas aqui](https://github.com/EuViniBlanco/api/tree/main/schemas)

## routes:
[Todos endpoints aqui](https://github.com/EuViniBlanco/api/tree/main/routes)