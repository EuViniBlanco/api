from fastapi import FastAPI
from routes.categoria import categoria

app = FastAPI()

app.include_router(categoria)