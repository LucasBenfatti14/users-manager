from pydantic import BaseModel

class PessoaResponse(BaseModel):
    id: int
    nome: str
    idade: int

class PessoaCreate(BaseModel):
    nome: str
    idade: int

class PessoaPatch(BaseModel):
    nome: str | None = None
    idade: int | None = None
