from fake_repository import FakeRepository
from services import PessoaService
from domain import Pessoa
from exceptions import PessoaJaCadastradaError
import pytest

def test_pessoa_service_rejeita_cadastro_duplicado() -> None:
    fake_repository = FakeRepository()
    pessoa_service = PessoaService(fake_repository)
    pessoa_1 = Pessoa(None, "Lucas Benfatti", 18)
    pessoa_2 = Pessoa(None, "Lucas Benfatti", 45)
    fake_id = pessoa_service.cadastrar(pessoa_1)
    pessoa_1.registrar_persistencia(fake_id)
    with pytest.raises(PessoaJaCadastradaError):
        pessoa_service.cadastrar(pessoa_2)

def test_pessoa_service_aceita_cadastro() -> None:
    fake_repository = FakeRepository()
    pessoa_service = PessoaService(fake_repository)
    pessoa = Pessoa(None, "Lucas Benfatti", 18)
    fake_id = pessoa_service.cadastrar(pessoa)
    assert fake_id == 1
