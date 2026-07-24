import sqlite3

class ConexaoBanco:

    def __init__(self, banco="pessoas.db"):
        self.banco = banco

    def __enter__(self):
        self.conexao = sqlite3.connect(self.banco)
        return self.conexao

    def __exit__(self, tipo, valor, traceback):
        if tipo is None:
            self.conexao.commit()
        else:
            self.conexao.rollback()
        self.conexao.close()

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

def cadastrar_nova_pessoa(nome:str, idade:int) -> bool:
    try:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            INSERT INTO pessoas (nome, idade)
            VALUES (?, ?)
        """,
            (nome, idade)
        )
            return True
    except sqlite3.Error:
        return False

def listar_pessoas() -> list[tuple[int, str, int]] | None:
    try:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            SELECT id, nome, idade FROM pessoas
        """)
            return cursor.fetchall()
    except sqlite3.Error:
        return None

def buscar_pessoa(id:int) -> tuple | None:
    try:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            SELECT id, nome, idade FROM pessoas
            WHERE id = ?
        """, (id,)
        )
            return cursor.fetchone()
    except sqlite3.Error:
        return None

def atualizar_pessoa(id:int, nome:str, idade:int) -> bool:
    try:
        with ConexaoBanco() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            UPDATE pessoas
            SET nome = ?, idade = ?
            WHERE id = ?
        """, (nome, idade, id)
        )
        if cursor.rowcount == 0:
            return False
        return True
    except sqlite3.Error:
        return False

def excluir_pessoa(id:int) -> bool:
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
