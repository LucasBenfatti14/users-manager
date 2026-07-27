import sqlite3
from .conexao import ConexaoBanco

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
    except sqlite3.Error:
        return False
