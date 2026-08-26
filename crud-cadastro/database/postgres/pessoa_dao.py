from .conexao import ConexaoPostgres
from domain import Pessoa
from repositories import PessoaRepository

class PessoaDAO(PessoaRepository):

    def cadastrar(self, pessoa:Pessoa) -> int:
        with ConexaoPostgres() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
        INSERT INTO pessoas (nome, idade)
        VALUES (%s, %s)
        RETURNING id
        """, (pessoa.nome, pessoa.idade))
        id_gerado = cursor.fetchone()[0]
        return id_gerado

    def listar(self) -> list[Pessoa]:
        with ConexaoPostgres() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            SELECT id, nome, idade FROM pessoas
            """)
            pessoas = []
            for id, nome, idade in cursor.fetchall():
                pessoas.append(Pessoa(id = id, nome = nome, idade = idade))
            return pessoas

    def buscar(self, id:int) -> Pessoa | None:
        with ConexaoPostgres() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            SELECT id, nome, idade FROM pessoas
            WHERE id = %s
            """, (id,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            id, nome, idade = dados
            return Pessoa(id = id, nome = nome, idade = idade)

    def buscar_por_nome(self, nome:str) -> Pessoa | None:
        with ConexaoPostgres() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            SELECT id, nome, idade FROM pessoas
            WHERE nome = %s
            """, (nome,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            id, nome, idade = dados
            return Pessoa(id = id, nome = nome, idade = idade)

    def atualizar(self, pessoa:Pessoa) -> None:
        with ConexaoPostgres() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            UPDATE pessoas
            SET nome = %s, idade = %s
            WHERE id = %s
            """, (pessoa.nome, pessoa.idade, pessoa.id))

    def excluir(self, id:int) -> bool:
        with ConexaoPostgres() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            DELETE FROM pessoas
            WHERE ID = %s
            """, (id,))
            if cursor.rowcount == 0:
                return False
            return True

    def existe_nome_em_outro_id(self, id:int, nome_novo:str) -> bool:
        with ConexaoPostgres() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            SELECT nome FROM pessoas
            WHERE id <> %s AND nome = %s
            """, (id, nome_novo))
            dado = cursor.fetchone()
            if dado is None:
                return False
            return True
