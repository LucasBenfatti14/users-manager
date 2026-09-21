from fake_repository import FakeRepository
from services import PessoaService
from domain import Pessoa
from exceptions import PessoaJaCadastradaError
import pytest

@pytest.fixture
def fake_repository():
    fake_repository = FakeRepository()
    return fake_repository

@pytest.fixture
def pessoa_service(fake_repository):
    pessoa_service = PessoaService(fake_repository)
    return pessoa_service


def test_pessoa_service_rejeita_cadastro_duplicado(pessoa_service) -> None:
    pessoa_1 = Pessoa(None, "Lucas Benfatti", 18)
    pessoa_2 = Pessoa(None, "Lucas Benfatti", 45)
    fake_id = pessoa_service.cadastrar(pessoa_1)
    pessoa_1.registrar_persistencia(fake_id)
    with pytest.raises(PessoaJaCadastradaError):
        pessoa_service.cadastrar(pessoa_2)

def test_pessoa_service_aceita_cadastro(pessoa_service) -> None:
    pessoa = Pessoa(None, "Lucas Benfatti", 18)
    fake_id = pessoa_service.cadastrar(pessoa)
    assert fake_id == 1

def test_pessoa_service_lista_pessoas(pessoa_service) -> None:
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

def test_pessoa_service_busca_e_encontra_pessoa(pessoa_service) -> None:
    pessoa = Pessoa(None, "Lucas Benfatti", 18)
    fake_id = pessoa_service.cadastrar(pessoa)
    pessoa.registrar_persistencia(fake_id)
    pessoa_encontrada = pessoa_service.buscar(1)
    assert pessoa_encontrada == pessoa

def test_pessoa_service_busca_e_nao_encontra_pessoa(pessoa_service) -> None:
    assert pessoa_service.buscar(1) is None

def test_pessoa_service_aceita_atualizacao_de_pessoa(pessoa_service) -> None:
    pessoa = Pessoa(None, "Lucas Benfatti", 18)
    fake_id = pessoa_service.cadastrar(pessoa)
    pessoa.registrar_persistencia(fake_id)
    pessoa_service.atualizar(pessoa, "John Doe", 40)
    pessoa_encontrada = pessoa_service.buscar(1)
    assert pessoa_encontrada.nome == "John Doe" and pessoa_encontrada.idade == 40

def test_pessoa_service_rejeita_atualizacao_de_pessoa_com_nome_duplicado(pessoa_service) -> None:
    pessoa_1 = Pessoa(None, "Lucas Benfatti", 18)
    pessoa_2 = Pessoa(None, "John Doe", 40)
    fake_id = pessoa_service.cadastrar(pessoa_1)
    pessoa_1.registrar_persistencia(fake_id)
    with pytest.raises(PessoaJaCadastradaError):
        pessoa_service.atualizar(pessoa_2, "Lucas Benfatti", 40)

def test_pessoa_service_exclui_pessoa_existente(pessoa_service) -> None:
    pessoa = Pessoa(None, "Lucas Benfatti", 18)
    fake_id = pessoa_service.cadastrar(pessoa)
    pessoa.registrar_persistencia(fake_id)
    assert pessoa_service.excluir(1) is True

def test_pessoa_service_nao_exclui_pessoa_nao_existente(pessoa_service) -> None:
    assert pessoa_service.excluir(1) is False

def test_pessoa_service_aceita_atualizacao_parcial_do_nome_de_pessoa(pessoa_service) -> None:
    pessoa = Pessoa(None, "Luc Benfatti", 18)
    fake_id = pessoa_service.cadastrar(pessoa)
    pessoa.registrar_persistencia(fake_id)
    pessoa_service.atualizar_parcialmente(pessoa, "Lucas Benfatti", None)
    pessoa_encontrada = pessoa_service.buscar(1)
    assert pessoa_encontrada.nome == "Lucas Benfatti" and pessoa_encontrada.idade == 18

def test_pessoa_service_aceita_atualizacao_parcial_da_idade_de_pessoa(pessoa_service) -> None:
    pessoa = Pessoa(None, "Lucas Benfatti", 20)
    fake_id = pessoa_service.cadastrar(pessoa)
    pessoa.registrar_persistencia(fake_id)
    pessoa_service.atualizar_parcialmente(pessoa, None, 18)
    pessoa_encontrada = pessoa_service.buscar(1)
    assert pessoa_encontrada.idade == 18 and pessoa_encontrada.nome == "Lucas Benfatti"

def test_pessoa_service_rejeita_atualizacao_parcial_do_nome_de_pessoa_ja_existente(pessoa_service) -> None:
    pessoa_1 = Pessoa(None, "Lucas Benfatti", 18)
    fake_id = pessoa_service.cadastrar(pessoa_1)
    pessoa_1.registrar_persistencia(fake_id)
    pessoa_2 = Pessoa(None, "John Doe", 40)
    with pytest.raises(PessoaJaCadastradaError):
        pessoa_service.atualizar_parcialmente(pessoa_2, "Lucas Benfatti", None)
