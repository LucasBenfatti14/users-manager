import sqlite3
from .conexao import ConexaoBanco
from .pessoa import Pessoa


class PessoaDAO:

    def cadastrar(self, nome:str, idade:int) -> Pessoa | None:
        try:
            with ConexaoBanco() as conexao:
                cursor = conexao.cursor()
                cursor.execute("""
                INSERT INTO pessoas (nome, idade)
                VALUES (?, ?)
            """,
                (nome, idade)
            )
                id_gerado = cursor.lastrowid
                return Pessoa(id = id_gerado, nome = nome, idade = idade)
        except sqlite3.Error:
            return None

    def listar(self) -> list[Pessoa] | None:
        try:
            with ConexaoBanco() as conexao:
                cursor = conexao.cursor()
                cursor.execute("""
                SELECT id, nome, idade FROM pessoas
            """)
                pessoas = []
                for id, nome, idade in cursor.fetchall():
                    pessoas.append(Pessoa(id = id, nome = nome, idade = idade))
                return pessoas
        except sqlite3.Error:
            return None

    def buscar(self, id:int) -> Pessoa | None:
        try:
            with ConexaoBanco() as conexao:
                cursor = conexao.cursor()
                cursor.execute("""
                SELECT id, nome, idade FROM pessoas
                WHERE id = ?
            """, (id,)
            )
                dados = cursor.fetchone()
                if dados is None:
                    return None
                id, nome, idade = dados
                return Pessoa(id = id, nome = nome, idade = idade)
        except sqlite3.Error:
            return None

    def atualizar(self, pessoa:Pessoa) -> bool:
        try:
            with ConexaoBanco() as conexao:
                cursor = conexao.cursor()
                cursor.execute("""
                UPDATE pessoas
                SET nome = ?, idade = ?
                WHERE id = ?
            """, (pessoa.nome, pessoa.idade, pessoa.id)
            )
            if cursor.rowcount == 0:
                return False
            return True
        except sqlite3.Error:
            return False

    def excluir(self, id:int) -> bool:
        try:
            with ConexaoBanco() as conexao:
                cursor = conexao.cursor()
                cursor.execute("""
                DELETE FROM pessoas
                WHERE id = ?
            """, (id,)
            )
            if cursor.rowcount == 0:
                return False
            return True
        except sqlite3.Error:
            return False
