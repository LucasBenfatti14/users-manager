from .conexao import ConexaoPostgres

def criar_tabela():
    with ConexaoPostgres() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            idade INTEGER NOT NULL
        );
    """)
