class DominioError(Exception):
    pass

class NomeInvalidoError(DominioError):
    pass

class IdJaDefinidoError(DominioError):
    pass

class NomeEIdadeNaoFornecidos(DominioError):
    pass

class IdadeInvalidaError(DominioError):
    pass

class NomeComCaracteresInvalidosError(NomeInvalidoError):
    pass

class NomeIncompletoError(NomeInvalidoError):
    pass
