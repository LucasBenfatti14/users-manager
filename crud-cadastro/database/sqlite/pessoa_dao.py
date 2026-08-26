from .conexao import ConexaoBanco
from domain import Pessoa
from repositories import PessoaRepository

class PessoaDAO(PessoaRepository):

    def cadastrar(self, pessoa:Pessoa) -> int:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            INSERT INTO pessoas (nome, idade)
            VALUES (?, ?)
            """, (pessoa.nome, pessoa.idade))
            return cursor.lastrowid

    def listar(self) -> list[Pessoa]:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            SELECT id, nome, idade FROM pessoas
            """)
            pessoas = []
            for id, nome, idade in cursor.fetchall():
                pessoas.append(Pessoa(id = id, nome = nome, idade = idade))
            return pessoas

    def buscar(self, id:int) -> Pessoa | None:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            SELECT id, nome, idade FROM pessoas
            WHERE id = ?
            """, (id,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            id, nome, idade = dados
            return Pessoa(id = id, nome = nome, idade = idade)

    def buscar_por_nome(self, nome:str) -> Pessoa | None:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            SELECT id, nome, idade FROM pessoas
            WHERE nome = ?
            """, (nome,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            id, nome, idade = dados
            return Pessoa(id = id, nome = nome, idade = idade)

    def atualizar(self, pessoa:Pessoa) -> None:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            UPDATE pessoas
            SET nome = ?, idade = ?
            WHERE id = ?
            """, (pessoa.nome, pessoa.idade, pessoa.id))

    def excluir(self, id:int) -> bool:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            DELETE FROM pessoas
            WHERE id = ?
            """, (id,))
            if cursor.rowcount == 0:
                return False
            return True

    def existe_nome_em_outro_id(self, id:int, nome_novo:str) -> bool:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            SELECT nome FROM pessoas
            WHERE id <> ? AND nome = ?
            """, (id, nome_novo))
            dado = cursor.fetchone()
            if dado is None:
                return False
            return True
