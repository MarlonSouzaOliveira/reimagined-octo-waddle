import random
from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool
@app.get("/")
def read_root():
    return {"message": "API rodando 🚀"}

@app.get("/hellooworld")
async def root():
    return {"message": "Hello Word"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 50000)}

@app.get("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.get("/estudantes/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0

@app.get("/estudantes/delete/{id_estudante}")
async def delete_item(id_estudante: int):
    return id_estudante > 0