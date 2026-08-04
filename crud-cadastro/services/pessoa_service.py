from repositories import PessoaRepository
from domain import Pessoa
from exceptions import (PessoaJaCadastradaError)

class PessoaService:

    def __init__(self, repository:PessoaRepository) -> None:
        self.repository = repository

    def cadastrar(self, pessoa:Pessoa) -> Pessoa:
        if self._nome_ja_existe(pessoa.nome):
            raise PessoaJaCadastradaError()
        id_gerado = self.repository.cadastrar(pessoa)
        pessoa._definir_id(id_gerado)
        return pessoa

    def listar(self) -> list[Pessoa]:
        return self.repository.listar()

    def buscar(self, id:int) -> Pessoa | None:
        return self.repository.buscar(id)

    def atualizar(self, pessoa:Pessoa) -> bool:
        if self._nome_ja_existe_atualizar(pessoa):
            raise PessoaJaCadastradaError()
        return self.repository.atualizar(pessoa)

    def excluir(self, id:int) -> bool:
        return self.repository.excluir(id)

    def _nome_ja_existe(self, nome:str) -> bool:
        if self.repository.buscar_por_nome(nome):
            return True
        return False

    def _nome_ja_existe_atualizar(self, pessoa:Pessoa) -> bool:
        return self.repository.buscar_para_atualizar(pessoa)
