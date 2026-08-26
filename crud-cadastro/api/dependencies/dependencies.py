from fastapi import Depends
from repositories import PessoaRepository
from services import PessoaService
from database.postgres import PessoaDAO

def get_repository() -> PessoaRepository:
    return PessoaDAO()

def get_service(repo: PessoaRepository = Depends(get_repository)) -> PessoaService:
    return PessoaService(repo)
