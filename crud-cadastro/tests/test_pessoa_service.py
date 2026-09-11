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

def test_pessoa_service_lista_pessoas() -> None:
    fake_repository = FakeRepository()
    pessoa_service = PessoaService(fake_repository)
    lista_pessoas_esperada = []
    pessoa_1 = Pessoa(None, "Lucas Benfatti", 18)
    pessoa_2 = Pessoa(None, "John Doe", 40)
    lista_pessoas_esperada.append(pessoa_1)
    lista_pessoas_esperada.append(pessoa_2)
    fake_id = pessoa_service.cadastrar(pessoa_1)
    pessoa_1.registrar_persistencia(fake_id)
    fake_id = pessoa_service.cadastrar(pessoa_2)
    pessoa_2.registrar_persistencia(fake_id)
    lista_pessoas = pessoa_service.listar()
    assert lista_pessoas == lista_pessoas_esperada

def test_pessoa_service_busca_e_encontra_pessoa() -> None:
    fake_repository = FakeRepository()
    pessoa_service = PessoaService(fake_repository)
    pessoa = Pessoa(None, "Lucas Benfatti", 18)
    fake_id = pessoa_service.cadastrar(pessoa)
    pessoa.registrar_persistencia(fake_id)
    pessoa_encontrada = pessoa_service.buscar(1)
    assert pessoa_encontrada == pessoa

def test_pessoa_service_busca_e_nao_encontra_pessoa() -> None:
    fake_repository = FakeRepository()
    pessoa_service = PessoaService(fake_repository)
    assert pessoa_service.buscar(1) is None
