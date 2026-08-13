import sqlite3
from pathlib import Path

class ConexaoBanco:

    def __init__(self, banco:str="pessoas.db") -> None:
        raiz_projeto = Path(__file__).resolve().parent.parent
        self.banco = raiz_projeto / banco

    def __enter__(self) -> sqlite3.Connection:
        self.conexao = sqlite3.connect(self.banco)
        return self.conexao

    def __exit__(self, tipo, valor, traceback):
        if tipo is None:
            self.conexao.commit()
        else:
            self.conexao.rollback()
        self.conexao.close()
