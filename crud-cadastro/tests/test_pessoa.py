import pytest
from domain import Pessoa
from exceptions import IdadeInvalidaError

@pytest.mark.parametrize("idade_valida", [0, 18, 130])
def test_pessoa_aceita_idade_valida(idade_valida):
    pessoa = Pessoa(None,"Lucas Benfatti", idade_valida)
    assert pessoa.idade == idade_valida

@pytest.mark.parametrize("idade_invalida", [-1, 131])
def test_pessoa_rejeita_idade_invalida(idade_invalida):
    with pytest.raises(IdadeInvalidaError):
        Pessoa(None, "Lucas Benfatti", idade_invalida)
