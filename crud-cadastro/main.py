from interface import (mostrar_menu, pedir_opcao, sair, linha, retornar, titulo, ler_nome, ler_idade, ler_id, mostrar_cadastros, mensagem_cadastro_realizado, formatar_erro, mensagem_alteracao_realizada, mensagem_exclusao_realizada, mostrar_cadastro_unico)
from database import (listar_pessoas, cadastrar_nova_pessoa, criar_tabela, buscar_pessoa, atualizar_pessoa, excluir_pessoa)


# Programa principal
if not criar_tabela():
    formatar_erro("BANCO DE DADOS INOPERANTE!")
    raise SystemExit
while True:
    mostrar_menu()
    opcao = pedir_opcao()
    if opcao == 0:
        sair()
        break
    match opcao:
        case 1:
            titulo("PESSOAS CADASTRADAS")
            mostrar_cadastros(listar_pessoas())
        case 2:
            titulo("NOVO CADASTRO")
            nome = ler_nome()
            if cadastrar_nova_pessoa(nome, ler_idade()):
                mensagem_cadastro_realizado(nome)
            else:
                formatar_erro("Não foi possível cadastrar uma nova pessoa. Tente novamente mais tarde!")
        case 3:
            titulo("BUSCAR CADASTRO")
            dado = buscar_pessoa(ler_id())
            if dado is None:
                formatar_erro("Não existe nenhuma pessoa cadastrada com esse ID!")
            elif dado:
                mostrar_cadastro_unico(dado)
            else:
                formatar_erro("Não foi possível buscar essa pessoa. Tente novamente mais tarde!")
        case 4:
            titulo("ATUALIZAR CADASTRO")
            id_pessoa = ler_id()
            nome_novo = ler_nome()
            idade_nova = ler_idade()
            if atualizar_pessoa(id_pessoa, nome_novo, idade_nova):
                mensagem_alteracao_realizada(nome_novo, idade_nova)
            else:
                formatar_erro("Não foi possível alterar os dados dessa pessoa. Tente novamente mais tarde!")
        case 5:
            titulo("EXCLUIR CADASTRO")
            if excluir_pessoa(ler_id()):
                mensagem_exclusao_realizada()
            else:
                formatar_erro("Não foi possível excluir esse registro. Tente novamente mais tarde!")
    linha()
    retornar()
            