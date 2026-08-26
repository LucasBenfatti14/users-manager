import psycopg
from exceptions import BancoDeDadosError
import os
from dotenv import load_dotenv

load_dotenv()

class ConexaoPostgres:

    def __enter__(self) -> psycopg.Connection:
        try:
            self.conexao = psycopg.connect(
                host=os.environ["POSTGRES_HOST"],
                port=os.environ["POSTGRES_PORT"],
                dbname=os.environ["POSTGRES_DB"],
                user=os.environ["POSTGRES_USER"],
                password=os.environ["POSTGRES_PASSWORD"]
            )
            return self.conexao
        except psycopg.Error as erro:
            raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro

    def __exit__(self, tipo, valor, traceback):
        try:
            if tipo is None:
                self.conexao.commit()
            else:
                self.conexao.rollback()
                if isinstance(valor, psycopg.Error):
                    raise BancoDeDadosError("Erro ao acessar o banco de dados.") from valor
        except psycopg.Error as erro:
            raise BancoDeDadosError("Erro ao acessar o banco de dados.") from erro
        finally:
            self.conexao.close()
