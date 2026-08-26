import sqlite3
from pathlib import Path
from exceptions import BancoDeDadosError

class ConexaoBanco:

    def __init__(self, banco:str="pessoas.db") -> None:
        raiz_projeto = Path(__file__).resolve().parent.parent.parent
        self.banco = raiz_projeto / banco

    def __enter__(self) -> sqlite3.Connection:
        try:
            self.conexao = sqlite3.connect(self.banco)
            return self.conexao
        except sqlite3.Error as erro:
            raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro

    def __exit__(self, tipo, valor, traceback):
        try:
            if tipo is None:
                self.conexao.commit()
            else:
                self.conexao.rollback()
                if isinstance(valor, sqlite3.Error):
                    raise BancoDeDadosError("Erro ao acessar o banco de dados.") from valor
        except sqlite3.Error as erro:
            raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro
        finally:
            self.conexao.close()
