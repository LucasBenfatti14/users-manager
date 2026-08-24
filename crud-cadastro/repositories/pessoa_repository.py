from abc import ABC, abstractmethod
from domain import Pessoa

class PessoaRepository(ABC):

    @abstractmethod
    def cadastrar(self, pessoa:Pessoa) -> int:
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
    def atualizar(self, pessoa:Pessoa) -> None:
        pass

    @abstractmethod
    def excluir(self, id:int) -> bool:
        pass

    @abstractmethod
    def existe_nome_em_outro_id(self, id:int, nome_novo:str) -> bool:
        pass
