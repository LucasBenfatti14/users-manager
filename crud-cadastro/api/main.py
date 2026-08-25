from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse, Response
from database import criar_tabela
from services import PessoaService
from .models import PessoaResponse, PessoaPatch, PessoaCreate
from domain import Pessoa
from exceptions import BancoDeDadosError, DominioError, RegraDeNegocioError
from .dependencies import get_service

app = FastAPI()

try:
    criar_tabela()
except BancoDeDadosError:
    raise SystemExit

@app.get("/pessoas", status_code=200)
def listar_pessoas(service:PessoaService = Depends(get_service)) -> list[PessoaResponse]:
    pessoas = service.listar()
    lista = []
    for pessoa in pessoas:
        lista.append(to_response(pessoa))
    return lista

@app.post("/pessoas", status_code=201)
def cadastrar_pessoa(dados:PessoaCreate, service:PessoaService = Depends(get_service)) -> PessoaResponse:
    pessoa = Pessoa(id=None, nome=dados.nome, idade=dados.idade)
    id_gerado = service.cadastrar(pessoa)
    pessoa.registrar_persistencia(id_gerado)
    return to_response(pessoa)

@app.put("/pessoas/{id}", status_code=200)
def atualizar_pessoa(id:int, dados:PessoaCreate, service:PessoaService = Depends(get_service)) -> PessoaResponse:
    pessoa = service.buscar(id)
    if pessoa is None:
        return JSONResponse(status_code=404, content={"detail": "Não existe nenhuma pessoa com esse ID."})
    service.atualizar(pessoa, dados.nome, dados.idade)
    return to_response(pessoa)

@app.patch("/pessoas/{id}", status_code=200)
def atualizar_pessoa_parcialmente(id:int, dados:PessoaPatch, service:PessoaService = Depends(get_service)) -> PessoaResponse:
    pessoa = service.buscar(id)
    if pessoa is None:
        return JSONResponse(status_code=404, content={"detail": "Não existe nenhuma pessoa com esse ID."})
    service.atualizar_parcialmente(pessoa, dados.nome, dados.idade)
    return to_response(pessoa)

@app.delete("/pessoas/{id}", status_code=204)
def excluir_pessoa(id:int, service:PessoaService = Depends(get_service)) -> Response:
    if not service.excluir(id):
        return JSONResponse(status_code=404, content={"detail": "Não existe nenhuma pessoa com esse ID."})
    return Response(status_code=204)

def to_response(pessoa:Pessoa) -> PessoaResponse:
    return PessoaResponse(
        id=pessoa.id,
        nome=pessoa.nome,
        idade=pessoa.idade
    )

@app.exception_handler(DominioError)
async def dominio_error_handler(request:Request, exc:DominioError):
    return JSONResponse(status_code=422, content={"detail": str(exc)})

@app.exception_handler(RegraDeNegocioError)
async def regra_de_negocio_error_handler(request:Request, exc:RegraDeNegocioError):
    return JSONResponse(status_code=409, content={"detail": str(exc)})

@app.exception_handler(BancoDeDadosError)
async def banco_de_dados_error_handler(request:Request, exc:BancoDeDadosError):
    return JSONResponse(status_code=500, content={"detail": "Não foi possível processar a solicitação."})
