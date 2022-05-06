# FastAPI - Python, MongoDB e Docker

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%40viniciusblanco-blue)](https://www.linkedin.com/in/viniciusblanco/)
### Install FastAPI
```
pip install "fastapi[all]"
```

You can also install it part by part.

This is what you would probably do once you want to deploy your application to production:

```
pip install fastapi
```
Also install uvicorn to work as the server:


```
pip install "uvicorn[standard]"
```

## what is uvicorn ?
Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

## What is pydentic model
You can think of models as similar to types in strictly typed languages, or as the requirements of a single endpoint in an API.

## Run server 
```
uvicorn main:app --reload
```

# Project structure
## models:
All database related files

## schemas:
All pydentic model files

## routers
All end point define here