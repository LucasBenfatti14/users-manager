import pytest
from domain import Pessoa
from exceptions import IdadeInvalidaError, NomeInvalidoError, NomeIncompletoError, NomeComCaracteresInvalidosError

@pytest.mark.parametrize("idade_valida", [0, 18, 130])
def test_pessoa_aceita_idade_valida(idade_valida: int) -> None:
    pessoa = Pessoa(None,"Lucas Benfatti", idade_valida)
    assert pessoa.idade == idade_valida

@pytest.mark.parametrize("idade_invalida", [-1, 131])
def test_pessoa_rejeita_idade_invalida(idade_invalida: int) -> None:
    with pytest.raises(IdadeInvalidaError):
        Pessoa(None, "Lucas Benfatti", idade_invalida)

@pytest.mark.parametrize("nome_nao_normalizado", ["lucas   benfatti", "lucas Benfatti  "])
def test_pessoa_normaliza_nome_completo(nome_nao_normalizado: str) -> None:
    pessoa = Pessoa(None, nome_nao_normalizado, 20)
    assert pessoa.nome == "Lucas Benfatti"

@pytest.mark.parametrize("primeiro_nome_valido", ["A" + "a" * 2 + " Pereira", "A" + "a" * 31 + " Pereira"])
def test_pessoa_aceita_primeiro_nome_valido(primeiro_nome_valido: str) -> None:
    pessoa = Pessoa(None, primeiro_nome_valido, 20)
    assert pessoa.nome == primeiro_nome_valido

@pytest.mark.parametrize("primeiro_nome_invalido", ["a" * 2 + " Pereira", "a" * 33 + " Pereira"])
def test_pessoa_rejeita_primeiro_nome_invalido(primeiro_nome_invalido: str) -> None:
    with pytest.raises(NomeInvalidoError):
        Pessoa(None, primeiro_nome_invalido, 20)

def test_pessoa_aceita_primeiro_nome_acentuado_valido() -> None:
    pessoa = Pessoa(None, "Áâãàç Pereira", 20)
    assert pessoa.nome == "Áâãàç Pereira"

@pytest.mark.parametrize("sobrenome_valido", ["Lucas " + "A" + "a", "Lucas " + "A" + "a" * 49])
def test_pessoa_aceita_sobrenome_valido(sobrenome_valido: str) -> None:
    pessoa = Pessoa(None, sobrenome_valido, 20)
    assert pessoa.nome == sobrenome_valido

@pytest.mark.parametrize("sobrenome_invalido", ["Lucas " + "a" * 1, "Lucas " + "a" * 51])
def test_pessoa_rejeita_sobrenome_invalido(sobrenome_invalido: str) -> None:
    with pytest.raises(NomeInvalidoError):
        Pessoa(None, sobrenome_invalido, 20)

@pytest.mark.parametrize("nome_incompleto", ["Lucas", "Mauro"])
def test_pessoa_rejeita_nome_incompleto(nome_incompleto: str) -> None:
    with pytest.raises(NomeIncompletoError):
        Pessoa(None, nome_incompleto, 20)

@pytest.mark.parametrize("nome_com_caracteres_invalidos", ["Luc4s Benfatti", "Luc@s Benf4tti", "Luc#s Benfatti"])
def test_pessoa_rejeita_caracteres_invalidos(nome_com_caracteres_invalidos: str) -> None:
    with pytest.raises(NomeComCaracteresInvalidosError):
        Pessoa(None, nome_com_caracteres_invalidos, 20)
