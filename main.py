from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

produtos = []

class Produto(BaseModel):
    nome: str
    preco: float = Field(..., gt=0)
    em_estoque: bool = True

@app.get("/")
def inicio():
    return {"status": "ok"}

@app.get("/saudacao/{nome}")
def saudacao(nome: str):
    return {"mensagem": f"Olá, {nome}!"}

@app.post("/produtos")
def cadastrar(produto: Produto):
    produtos.append(produto)
    return {
        "mensagem": "Produto cadastrado com sucesso",
        **produto.model_dump()
    }

@app.get("/produtos")
def listar():
    return produtos

@app.get("/produtos/{indice}")
def buscar(indice: int):
    if indice < 0 or indice >= len(produtos):
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )
    return produtos[indice]