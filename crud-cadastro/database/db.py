import sqlite3
from .conexao import ConexaoBanco
from exceptions import BancoDeDadosError

def criar_tabela() -> bool:
    try:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
            )
        """)
            return True
    except sqlite3.Error as erro:
        raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro
