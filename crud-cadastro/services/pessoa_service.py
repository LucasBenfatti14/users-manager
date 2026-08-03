from repositories import PessoaRepository
from domain import Pessoa
from exceptions import (PessoaJaCadastradaError, NomeInvalidoError, IdadeInvalidaError)

class PessoaService:

    def __init__(self, repository:PessoaRepository) -> None:
        self.repository = repository

    def cadastrar(self, pessoa:Pessoa) -> Pessoa:
        self._normalizar_nome(pessoa)
        if not self._validar_nome(pessoa.nome):
            raise NomeInvalidoError()
        if not self._validar_idade(pessoa.idade):
            raise IdadeInvalidaError()
        if self._nome_ja_existe(pessoa.nome):
            raise PessoaJaCadastradaError()
        return self.repository.cadastrar(pessoa)

    def listar(self) -> list[Pessoa]:
        return self.repository.listar()

    def buscar(self, id:int) -> Pessoa | None:
        return self.repository.buscar(id)

    def atualizar(self, pessoa:Pessoa) -> bool:
        self._normalizar_nome(pessoa)
        if not self._validar_nome(pessoa.nome):
            raise NomeInvalidoError()
        if not self._validar_idade(pessoa.idade):
            raise IdadeInvalidaError()
        if self._nome_ja_existe_atualizar(pessoa):
            raise PessoaJaCadastradaError()
        return self.repository.atualizar(pessoa)

    def excluir(self, id:int) -> bool:
        return self.repository.excluir(id)

    def _normalizar_nome(self, pessoa:Pessoa) -> None:
        pessoa.nome = pessoa.nome.strip()
        nome_completo = pessoa.nome.split()
        nome_completo_normalizado = []
        for nome in nome_completo:
            nome = nome.capitalize()
            nome_completo_normalizado.append(nome)
        pessoa.nome = " ".join(nome_completo_normalizado)

    def _validar_nome(self, nome:str) -> bool:
        nome_completo = nome.split()
        if not nome_completo:
            return False
        for i, nome_pessoa in enumerate(nome_completo):
            if i == 0:
                if len(nome_pessoa) < 3 or len(nome_pessoa) > 32:
                    return False
            else:
                if len(nome_pessoa) < 2 or len(nome_pessoa) > 50:
                    return False
        return True

    def _validar_idade(self, idade:int) -> bool:
        if idade < 0 or idade >= 150:
            return False
        return True

    def _nome_ja_existe(self, nome:str) -> bool:
        if self.repository.buscar_por_nome(nome):
            return True
        return False

    def _nome_ja_existe_atualizar(self, pessoa:Pessoa) -> bool:
        return self.repository.buscar_para_atualizar(pessoa)
