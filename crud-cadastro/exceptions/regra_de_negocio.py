class RegraDeNegocioError(Exception):
    pass

class PessoaJaCadastradaError(RegraDeNegocioError):
    pass

class NomeInvalidoError(RegraDeNegocioError):
    pass

class IdadeInvalidaError(RegraDeNegocioError):
    pass
