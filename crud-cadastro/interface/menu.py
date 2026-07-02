from time import sleep
import os


ANSI = {
    "preto": "\033[30m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "magenta": "\033[35m",
    "ciano": "\033[36m",
    "branco": "\033[37m",

    "bg_preto": "\033[40m",
    "bg_vermelho": "\033[41m",
    "bg_verde": "\033[42m",
    "bg_amarelo": "\033[43m",
    "bg_azul": "\033[44m",
    "bg_magenta": "\033[45m",
    "bg_ciano": "\033[46m",
    "bg_branco": "\033[47m",

    "reset": "\033[m",
    "negrito": "\033[1m",
    "sublinhado": "\033[4m"
}


def linha(tam:int = 50) -> None:
    print("-" * tam)


def titulo(msg:str, tam:int=50) -> None:
    linha(tam)
    print(f"{ANSI['negrito']}{ANSI['bg_ciano']}{msg.center(tam)}{ANSI['reset']}")
    linha(tam)


def mostrar_menu() -> None:
    limpar_terminal()
    titulo("MENU PRINCIPAL")
    print(f"{ANSI['bg_azul']} 1 {ANSI['reset']} - {ANSI['negrito']}Ver pessoas cadastradas{ANSI['reset']}")
    print(f"{ANSI['bg_verde']} 2 {ANSI['reset']} - {ANSI['negrito']}Cadastrar nova pessoa{ANSI['reset']}")
    print(f"{ANSI['bg_vermelho']} 3 {ANSI['reset']} - {ANSI['negrito']}Sair do sistema{ANSI['reset']}")
    linha()


def formatar_erro(msg) -> None:
    print(f"{ANSI['bg_vermelho']}{"ERRO! "}{msg}{ANSI['reset']}")


def mostrar_cadastros(cadastros:list|None) -> None:
    if cadastros is None:
        formatar_erro("O arquivo não pôde ser aberto.")
    else:
        if not cadastros:
            print(f"{ANSI['amarelo']}Não há nenhum cadastro ainda!{ANSI['reset']}\nVolte ao menu para começar a cadastrar.")
        else:
            for nome, idade in cadastros:
                print(f"{nome:<40}{idade:>3} anos")


def mensagem_erro_arquivo_nao_criado() -> None:
    formatar_erro("O arquivo não foi criado.")


def mensagem_erro_cadastro() -> None:
    formatar_erro("O cadastro não pôde ser finalizado.")


def mensagem_cadastro_realizado(nome:str) -> None:
    print(f"{ANSI['bg_verde']}Novo registro adicionado: {ANSI['negrito']}{ANSI['sublinhado']}{nome} {ANSI['reset']}")


def leia_int(txt:str) -> int:
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            formatar_erro("Digite um número inteiro válido.")
            continue
        except KeyboardInterrupt:
            formatar_erro("O usuário optou por não inserir um número!")
            return 0
        else:
            return num
        

def leia_str(txt:str) -> str:
    while True:
        nome = input(txt).strip()
        if nome.isdigit():
            formatar_erro("Digite um nome contendo apenas caracteres texto.")
        elif nome == "":
            formatar_erro("O nome não pode ser vazio.")
        elif len(nome) <= 2:
            formatar_erro("O nome precisa ter mais que 2 caracteres.")
        else:
            return nome


def pedir_opcao() -> int:
    while True:
        opc = leia_int("Sua Opção: ")
        if opc < 0 or opc > 3:
            formatar_erro("Digite uma opção válida.")
        else:
            return opc
        

def ler_nome() -> str:
    nomes_lista = []
    nome = leia_str("Nome: ").split()
    for palavra in nome:
        nomes_lista.append(palavra.capitalize())
    nome_completo = " ".join(nomes_lista)
    return nome_completo


def ler_idade() -> int:
    while True:
        idade = leia_int("Idade: ")
        if idade < 0 or len(str(idade)) > 3:
            formatar_erro("Essa idade não é válida.")
            continue
        return idade
    

def sair() -> None:
    titulo("Saindo do sistema... Até logo!!")
    sleep(1.5)


def limpar_terminal() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def retornar() -> None:
    sleep(1)
    input(f"{ANSI['verde']}Pressione ENTER para voltar ao menu{ANSI['reset']} ")
