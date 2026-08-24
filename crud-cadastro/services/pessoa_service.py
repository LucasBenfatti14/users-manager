from repositories import PessoaRepository
from domain import Pessoa
from exceptions import (PessoaJaCadastradaError)

class PessoaService:

    def __init__(self, repository:PessoaRepository) -> None:
        self.repository = repository

    def cadastrar(self, pessoa:Pessoa) -> int:
        if self._nome_ja_existe(pessoa.nome):
            raise PessoaJaCadastradaError("Esse nome já foi cadastrado.")
        return self.repository.cadastrar(pessoa)

    def listar(self) -> list[Pessoa]:
        return self.repository.listar()

    def buscar(self, id:int) -> Pessoa | None:
        return self.repository.buscar(id)

    def atualizar(self, pessoa:Pessoa, nome_novo:str, idade_nova:int) -> None:
        if self._nome_ja_existe_atualizar(pessoa.id, nome_novo):
            raise PessoaJaCadastradaError("Esse nome já foi cadastrado.")
        pessoa.atualizar(nome_novo, idade_nova)
        self.repository.atualizar(pessoa)

    def atualizar_parcialmente(self, pessoa:Pessoa, nome_novo:str|None, idade_nova:int|None) -> None:
        if nome_novo is not None:
            if self._nome_ja_existe_atualizar(pessoa.id, nome_novo):
                raise PessoaJaCadastradaError("Esse nome já foi cadastrado.")
        pessoa.atualizar_parcialmente(nome_novo, idade_nova)
        self.repository.atualizar(pessoa)

    def excluir(self, id:int) -> bool:
        return self.repository.excluir(id)

    def _nome_ja_existe(self, nome:str) -> bool:
        if self.repository.buscar_por_nome(nome):
            return True
        return False

    def _nome_ja_existe_atualizar(self, id:int, nome_novo:str) -> bool:
        nome_novo = Pessoa.normalizar_nome(nome_novo)
        return self.repository.existe_nome_em_outro_id(id, nome_novo)
