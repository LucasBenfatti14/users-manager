import sqlite3


def conectar() -> sqlite3.Connection:
    return sqlite3.connect("pessoas.db")

def criar_tabela() -> bool:
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    """)
        conexao.commit()
        return True
    except sqlite3.Error:
        return False
    finally:
        if conexao:
            conexao.close()

def cadastrar_nova_pessoa(nome:str, idade:int) -> bool:
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        INSERT INTO pessoas (nome, idade)
        VALUES (?, ?)
    """,
        (nome, idade)
    )
        conexao.commit()
        return True
    except sqlite3.Error:
        if conexao:
            conexao.rollback()
        return False
    finally:
        if conexao:
            conexao.close()

def listar_pessoas() -> tuple | None:
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        SELECT id, nome, idade FROM pessoas
    """)
        dados = cursor.fetchall()
        return dados
    except sqlite3.Error:
        return None
    finally:
        if conexao:
            conexao.close()

def buscar_pessoa(id:int) -> tuple | None:
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        SELECT id, nome, idade FROM pessoas
        WHERE id = ?
    """, (id,)
    )
        return cursor.fetchone()
    except sqlite3.Error:
        return None
    finally:
        if conexao:
            conexao.close()

def atualizar_pessoa(id:int, nome:str, idade:int) -> bool:
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        UPDATE pessoas
        SET nome = ?, idade = ?
        WHERE id = ?
    """, (nome, idade, id)
    )
        conexao.commit()
        if cursor.rowcount == 0:
            return False
        return True
    except sqlite3.Error:
        return False
    finally:
        if conexao:
            conexao.close()

def excluir_pessoa(id:int) -> bool:
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        DELETE FROM pessoas
        WHERE id = ?
    """, (id,)
    )
        conexao.commit()
        if cursor.rowcount == 0:
            return False
        return True
    except sqlite3.Error:
        return False
    finally:
        if conexao:
            conexao.close()
