from fastapi import FastAPI
from database import criar_tabela
from database import PessoaDAO
from services import PessoaService
from api.models import PessoaResponse, PessoaCreate
from domain import Pessoa
from exceptions import BancoDeDadosError
from interface import formatar_erro

app = FastAPI()

pessoa_repository = PessoaDAO()
pessoa_service = PessoaService(pessoa_repository)
try:
    criar_tabela()
except BancoDeDadosError:
    raise SystemExit

@app.get("/pessoas")
def listar_pessoas():
    pessoas = pessoa_service.listar()
    lista = []
    for pessoa in pessoas:
        lista.append(to_response(pessoa))
    return lista

@app.post("/pessoas")
def cadastrar_pessoa(dados: PessoaCreate) -> PessoaResponse:
    pessoa = Pessoa(id=None, nome=dados.nome, idade=dados.idade)
    id_gerado = pessoa_service.cadastrar(pessoa)
    pessoa.registrar_persistencia(id_gerado)
    return to_response(pessoa)

def to_response(pessoa: Pessoa) -> PessoaResponse:
    return PessoaResponse(
        id=pessoa.id,
        nome=pessoa.nome,
        idade=pessoa.idade
    )
