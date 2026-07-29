from database.pessoa_dao import PessoaDAO
from database.pessoa import Pessoa

class PessoaService:

    def __init__(self, dao:PessoaDAO) -> None:
        self.dao = dao

    def cadastrar(self, pessoa:Pessoa) -> Pessoa | None:
        self._normalizar_nome(pessoa)
        nome_completo = pessoa.nome.split()
        for i, nome in enumerate(nome_completo):
            if i == 0:
                if len(nome) < 3 or len(nome) > 32:
                    return None
            else:
                if len(nome) < 2 or len(nome) > 50:
                    return None
        if pessoa.idade < 0:
            return None
        if self.dao.buscar_por_nome(pessoa.nome):
            return None
        return self.dao.cadastrar(pessoa)

    def listar(self) -> list[Pessoa] | None:
        return self.dao.listar()

    def buscar(self, id:int) -> Pessoa | None:
        return self.dao.buscar(id)

    def atualizar(self, pessoa:Pessoa) -> bool:
        return self.dao.atualizar(pessoa)

    def excluir(self, id:int) -> bool:
        return self.dao.excluir(id)

    def _normalizar_nome(self, pessoa:Pessoa) -> None:
        pessoa.nome = pessoa.nome.strip()
        nome_completo = pessoa.nome.split()
        nome_completo_normalizado = []
        for nome in nome_completo:
            nome = nome.capitalize()
            nome_completo_normalizado.append(nome)
        pessoa.nome = " ".join(nome_completo_normalizado)
