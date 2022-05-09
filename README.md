# FastAPI - Python, MongoDB e Docker

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%40viniciusblanco-blue)](https://www.linkedin.com/in/viniciusblanco/)

Versões utilizadas no projeto [aqui](https://github.com/EuViniBlanco/api/blob/main/requirements.txt)

### Instale o Anaconda

Link para baixar [aqui](https://www.anaconda.com/products/distribution)
### Instalando o ambiente virtual com a versão utilizada do python
```
conda create --name api-mongo python=3.10.4
```

Agora, deve-se ativar o ambiente virtual criado como ambiente principal
```
conda activate api-mongo
```
### Instalando FastAPI

```
pip install fastapi
```
Instale o uvicorn para trabalhar como nosso servidor:


```
pip install uvicorn
```

## Iniciar server 
```
uvicorn app:app --port 8086 --reload
```
Escolhi aqui a porta `:8086` para evitar conflitos com o sistema operacional, e o argumento `--reload` para poder sempre testar a API sem precisar matar o serviço do server e iniciar novamente
## Acessar a API via FastAPI
`*` http://localhost:8086/api/v1

Para acessar o teste da API, basta acessar o Swagger (`/docs`):

`*` http://localhost:8086/api/v1/docs

Os endpoints utilizados foram `/cadastro` (ou `/cadastros`) e `/produto` (ou `/produtos`)

`*`Obs.: caso execute a aplicação em um servidor web, trocar localhost pelo endereço de IP externo ou DNS


# Estrutura do Projeto:
## models:
[Todos arquivos de models aqui](https://github.com/EuViniBlanco/api/tree/main/models)

## schemas:
[Todos arquivos de Schemas aqui](https://github.com/EuViniBlanco/api/tree/main/schemas)

## routes:
[Todos endpoints aqui](https://github.com/EuViniBlanco/api/tree/main/routes)