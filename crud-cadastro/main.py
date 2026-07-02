from interface import (mostrar_menu, pedir_opcao, sair, mensagem_erro_arquivo_nao_criado, linha, retornar, titulo, ler_nome, ler_idade, mostrar_cadastros, mensagem_erro_cadastro, mensagem_cadastro_realizado)
from database import (arquivo_existe, criar_arquivo, ler_arquivo, cadastrar_nova_pessoa)


# Programa principal
if not arquivo_existe():
    if not criar_arquivo():
        mensagem_erro_arquivo_nao_criado()
while True:
    mostrar_menu()
    opcao = pedir_opcao()
    if opcao in (0,3):
        sair()
        break
    match opcao:
        case 1:
            titulo("PESSOAS CADASTRADAS")
            cadastros = ler_arquivo()
            mostrar_cadastros(cadastros)
            linha()
            retornar()
        case 2:
            titulo("NOVO CADASTRO")
            nome = ler_nome()
            idade = ler_idade()
            if not cadastrar_nova_pessoa(nome, idade):
                mensagem_erro_cadastro()
            else:
                mensagem_cadastro_realizado(nome)
            linha()
            retornar()
