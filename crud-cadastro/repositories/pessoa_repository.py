from abc import ABC, abstractmethod
from domain import Pessoa

class PessoaRepository(ABC):

    @abstractmethod
    def cadastrar(self, pessoa:Pessoa) -> Pessoa:
        pass

    @abstractmethod
    def listar(self) -> list[Pessoa]:
        pass

    @abstractmethod
    def buscar(self, id:int) -> Pessoa | None:
        pass

    @abstractmethod
    def buscar_por_nome(self, nome:str) -> Pessoa | None:
        pass

    @abstractmethod
    def atualizar(self, pessoa:Pessoa) -> bool:
        pass

    @abstractmethod
    def excluir(self, id:int) -> bool:
        pass

    @abstractmethod
    def buscar_para_atualizar(self, pessoa:Pessoa) -> bool:
        pass
