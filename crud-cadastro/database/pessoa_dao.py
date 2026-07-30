import sqlite3
from .conexao import ConexaoBanco
from .pessoa import Pessoa
from exceptions import BancoDeDadosError


class PessoaDAO:

    def cadastrar(self, pessoa:Pessoa) -> Pessoa | None:
        try:
            with ConexaoBanco() as conexao:
                cursor = conexao.cursor()
                cursor.execute("""
                INSERT INTO pessoas (nome, idade)
                VALUES (?, ?)
            """,
                (pessoa.nome, pessoa.idade)
            )
                pessoa.id = cursor.lastrowid
                return pessoa
        except sqlite3.Error as erro:
            raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro

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
        except sqlite3.Error as erro:
            raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro

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
        except sqlite3.Error as erro:
            raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro

    def buscar_por_nome(self, nome:str) -> Pessoa | None:
        try:
            with ConexaoBanco() as conexao:
                cursor = conexao.cursor()
                cursor.execute("""
                SELECT id, nome, idade FROM pessoas
                WHERE nome = ?
            """, (nome,)
            )
                dados = cursor.fetchone()
                if dados is None:
                    return None
                id, nome, idade = dados
                return Pessoa(id = id, nome = nome, idade = idade)
        except sqlite3.Error as erro:
            raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro

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
        except sqlite3.Error as erro:
            raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro

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
        except sqlite3.Error as erro:
            raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro

    def buscar_para_atualizar(self, pessoa:Pessoa) -> bool:
        try:
            with ConexaoBanco() as conexao:
                cursor = conexao.cursor()
                cursor.execute("""
                SELECT nome FROM pessoas
                WHERE id <> ? AND nome = ?
            """, (pessoa.id, pessoa.nome))
                dado = cursor.fetchone()
                if dado is None:
                    return False
                return True
        except sqlite3.Error as erro:
            raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro
