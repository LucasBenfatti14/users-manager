from .conexao import ConexaoBanco

def criar_tabela() -> None:
    with ConexaoBanco() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    """)
