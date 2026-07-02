ARQUIVO_PESSOAS = "pessoas-cadastradas.txt"


def arquivo_existe(a:str = ARQUIVO_PESSOAS) -> bool:
    try:
        with open(a, "rt"):
            pass
    except FileNotFoundError:
        return False
    return True


def criar_arquivo(a:str = ARQUIVO_PESSOAS) -> bool:
    try:
        with open(a, "wt+"):
            pass
    except OSError:
        return False
    return True


def ler_arquivo() -> list[str] | None:
    try:
        with open(ARQUIVO_PESSOAS, "rt") as a:
            pessoas = []
            for linha in a:
                nome, idade = linha.strip().split(";")
                pessoas.append((nome, int(idade)))
            return pessoas
    except OSError:
        return None


def cadastrar_nova_pessoa(nome:str, idade:int) -> bool:
    try:
        with open(ARQUIVO_PESSOAS, "at") as a:
            a.write(f"{nome};{idade}\n")
    except OSError:
        return False
    return True
