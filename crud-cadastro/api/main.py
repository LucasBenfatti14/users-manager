from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from database import criar_tabela
from database import PessoaDAO
from services import PessoaService
from api.models import PessoaResponse, PessoaCreate
from domain import Pessoa
from exceptions import BancoDeDadosError, DominioError, RegraDeNegocioError
from interface import formatar_erro

app = FastAPI()

pessoa_repository = PessoaDAO()
pessoa_service = PessoaService(pessoa_repository)
try:
    criar_tabela()
except BancoDeDadosError:
    raise SystemExit

@app.get("/pessoas")
def listar_pessoas() -> list[PessoaResponse]:
    pessoas = pessoa_service.listar()
    lista = []
    for pessoa in pessoas:
        lista.append(to_response(pessoa))
    return lista

@app.post("/pessoas")
def cadastrar_pessoa(dados:PessoaCreate) -> PessoaResponse:
    pessoa = Pessoa(id=None, nome=dados.nome, idade=dados.idade)
    id_gerado = pessoa_service.cadastrar(pessoa)
    pessoa.registrar_persistencia(id_gerado)
    return to_response(pessoa)

@app.put("/pessoas/{id}")
def atualizar_pessoa(id:int, dados:PessoaCreate) -> PessoaResponse:
    pessoa = pessoa_service.buscar(id)
    if pessoa is None:
        return JSONResponse(status_code=404, content={"detail": "Não existe nenhuma pessoa com esse ID."})
    pessoa_service.atualizar(pessoa, dados.nome, dados.idade)
    return to_response(pessoa)

def to_response(pessoa:Pessoa) -> PessoaResponse:
    return PessoaResponse(
        id=pessoa.id,
        nome=pessoa.nome,
        idade=pessoa.idade
    )

@app.exception_handler(DominioError)
async def dominio_error_handler(request: Request, exc: DominioError):
    return JSONResponse(status_code=422, content={"detail": str(exc)})

@app.exception_handler(RegraDeNegocioError)
async def regra_de_negocio_error_handler(request: Request, exc: RegraDeNegocioError):
    return JSONResponse(status_code=409, content={"detail": str(exc)})

@app.exception_handler(BancoDeDadosError)
async def banco_de_dados_error_handler(request: Request, exc: BancoDeDadosError):
    return JSONResponse(status_code=500, content={"detail": "Não foi possível processar a solicitação."})
