from domain import Pessoa
from repositories import PessoaRepository

lista_pessoas = []

class FakeRepository(PessoaRepository):

    def cadastrar(self, pessoa: Pessoa) -> int:
        contador = 0
        lista_pessoas.append(pessoa)
        for pessoa in lista_pessoas:
            contador += 1
        return contador
    
    def listar(self) -> list[Pessoa]:
        return lista_pessoas

    def buscar(self, id:int) -> Pessoa | None:
        for pessoa in lista_pessoas:
            if pessoa.id == id:
                return pessoa
        return None

    def buscar_por_nome(self, nome:str) -> Pessoa | None:
        for pessoa in lista_pessoas:
            if pessoa.nome == nome:
                return pessoa
        return None

    def atualizar(self, pessoa:Pessoa) -> None:
        for pessoa_lista in lista_pessoas:
            if pessoa_lista.id == pessoa.id:
                pessoa_lista.nome = pessoa.nome
                pessoa_lista.idade = pessoa.idade

    def excluir(self, id:int) -> bool:
        for pessoa in lista_pessoas:
            if pessoa.id == id:
                lista_pessoas.pop(lista_pessoas.index(pessoa))
                return True
        return False

    def existe_nome_em_outro_id(self, id:int, nome_novo:str) -> bool:
        for pessoa in lista_pessoas:
            if pessoa.nome == nome_novo and pessoa.id != id:
                return True
        return False
    