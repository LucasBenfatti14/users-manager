from domain import Pessoa
from time import sleep
import os

TAMANHO_PADRAO_LINHA = 50
ESPACO_MAX_PARA_NOME = 38
ESPACO_MAX_PARA_IDADE = 3
MENOR_OPCAO = 0
MAIOR_OPCAO = 5
TEMPO_PARA_RETORNAR_AO_MENU = 1
TEMPO_PARA_ENCERRAR_EXECUCAO = 1.5

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

def linha(tam:int=TAMANHO_PADRAO_LINHA) -> None:
    print("-" * tam)

def titulo(msg:str, tam:int=TAMANHO_PADRAO_LINHA) -> None:
    linha(tam)
    print(f"{ANSI['negrito']}{ANSI['bg_ciano']}{msg.center(tam)}{ANSI['reset']}")
    linha(tam)

def mostrar_menu() -> None:
    limpar_terminal()
    titulo("MENU PRINCIPAL")
    print(f"{ANSI['bg_vermelho']} 0 {ANSI['reset']} - {ANSI['negrito']}Sair do sistema{ANSI['reset']}")
    print(f"{ANSI['bg_azul']} 1 {ANSI['reset']} - {ANSI['negrito']}Ver pessoas cadastradas{ANSI['reset']}")
    print(f"{ANSI['bg_verde']} 2 {ANSI['reset']} - {ANSI['negrito']}Cadastrar nova pessoa{ANSI['reset']}")
    print(f"{ANSI['bg_amarelo']} 3 {ANSI['reset']} - {ANSI['negrito']}Buscar cadastro de uma pessoa{ANSI['reset']}")
    print(f"{ANSI['bg_magenta']} 4 {ANSI['reset']} - {ANSI['negrito']}Atualizar cadastro de uma pessoa{ANSI['reset']}")
    print(f"{ANSI['bg_ciano']} 5 {ANSI['reset']} - {ANSI['negrito']}Excluir uma pessoa cadastrada{ANSI['reset']}")
    linha()

def formatar_erro(msg:str) -> None:
    print(f"{ANSI['bg_vermelho']}{"ERRO! "}{msg}{ANSI['reset']}")

def mensagem_sem_cadastros() -> None:
    print(f"{ANSI['amarelo']}Não há nenhum cadastro ainda!{ANSI['reset']}\nVolte ao menu para começar a cadastrar.")

def mostrar_cadastros(pessoas:list[Pessoa]) -> None:
    for pessoa in pessoas:
        mostrar_cadastro_unico(pessoa)

def mostrar_cadastro_unico(pessoa:Pessoa) -> None:
    print(f"{pessoa.id} - {pessoa.nome:<{ESPACO_MAX_PARA_NOME}}{pessoa.idade:>{ESPACO_MAX_PARA_IDADE}} anos")

def mensagem_cadastro_realizado(nome:str) -> None:
    print(f"{ANSI['bg_verde']}Novo registro adicionado: {ANSI['negrito']}{ANSI['sublinhado']}{nome} {ANSI['reset']}")

def mensagem_alteracao_realizada(nome:str, idade:int) -> None:
    print(f"{ANSI['bg_verde']}O registro foi alterado com sucesso para: {ANSI['negrito']}{ANSI['sublinhado']}{nome} | {idade} anos {ANSI['reset']}")

def mensagem_exclusao_realizada() -> None:
    print(f"{ANSI['bg_verde']}Exclusão realizada com sucesso!{ANSI['negrito']}{ANSI['reset']}")

def ler_int(txt:str) -> int:
    while True:
        try:
            inteiro = int(input(txt))
            return inteiro
        except KeyboardInterrupt:
            formatar_erro("O usuário optou por não inserir um número!")
            raise SystemExit
        except ValueError:
            formatar_erro("Digite um número inteiro válido!")

def ler_str(txt:str) -> str:
    try:
        string = input(txt)
        return string
    except KeyboardInterrupt:
        formatar_erro("O usuário optou por não inserir um texto!")
        raise SystemExit

def ler_idade() -> int:
    idade = ler_int("Idade: ")
    return idade

def ler_nome() -> str:
    nome = ler_str("Nome: ")
    return nome

def pedir_opcao() -> int:
    while True:
        opc = ler_int("Sua Opção: ")
        if opc < MENOR_OPCAO or opc > MAIOR_OPCAO:
            formatar_erro("Digite uma opção válida.")
        else:
            return opc    

def ler_id() -> int:
    while True:
        id = ler_int("ID do usuário: ")
        if id <= 0:
            formatar_erro("Esse ID não é válido.")
            continue
        return id

def sair() -> None:
    titulo("Saindo do sistema... Até logo!!")
    sleep(TEMPO_PARA_ENCERRAR_EXECUCAO)

def limpar_terminal() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def retornar() -> None:
    sleep(TEMPO_PARA_RETORNAR_AO_MENU)
    input(f"{ANSI['verde']}Pressione ENTER para voltar ao menu{ANSI['reset']} ")
