class DominioError(Exception):
    pass

class NomeInvalidoError(DominioError):
    pass

class NomeComCaracteresInvalidosError(NomeInvalidoError):
    pass

class NomeIncompletoError(NomeInvalidoError):
    pass

class IdadeInvalidaError(DominioError):
    pass
