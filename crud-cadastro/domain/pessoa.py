from exceptions import (NomeInvalidoError, NomeIncompletoError, NomeComCaracteresInvalidosError, IdadeInvalidaError, IdJaDefinidoError)

class Pessoa:

    def __init__(self, id:int | None, nome:str, idade:int) -> None:
        self._id = id
        self.nome = nome
        self.idade = idade

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        valor = self._normalizar_nome(valor)
        self._validar_nome(valor)
        self._nome = valor

    @property
    def idade(self):
         return self._idade

    @idade.setter
    def idade(self, valor):
        self._validar_idade(valor)
        self._idade = valor

    def _validar_nome(self, nome:str) -> None:
            nome_completo = nome.split()
            if len(nome_completo) <= 1:
                raise NomeIncompletoError()
            for i, nome_pessoa in enumerate(nome_completo):
                if not nome_pessoa.isalpha():
                    raise NomeComCaracteresInvalidosError()
                if i == 0:
                    if len(nome_pessoa) < 3 or len(nome_pessoa) > 32:
                        raise NomeInvalidoError()
                else:
                    if len(nome_pessoa) < 2 or len(nome_pessoa) > 50:
                        raise NomeInvalidoError()

    def _normalizar_nome(self, nome:str) -> str:
            nome = nome.strip()
            nome_completo = nome.split()
            nome_completo_normalizado = []
            for nome in nome_completo:
                nome = nome.capitalize()
                nome_completo_normalizado.append(nome)
            nome = " ".join(nome_completo_normalizado)
            return nome

    def _validar_idade(self, idade:int) -> None:
            if idade < 0 or idade >= 150:
                raise IdadeInvalidaError()

    def registrar_persistencia(self, id_gerado:int) -> None:
        if self._id is not None:
            raise IdJaDefinidoError()
        self._id = id_gerado
