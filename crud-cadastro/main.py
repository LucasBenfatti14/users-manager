from interface import (mostrar_menu, pedir_opcao, sair, linha, retornar, titulo, ler_nome, ler_idade, ler_id, mostrar_cadastros, mensagem_cadastro_realizado, formatar_erro, mensagem_alteracao_realizada, mensagem_exclusao_realizada, mostrar_cadastro_unico)
from database import criar_tabela
from database.pessoa_dao import PessoaDAO
from services import PessoaService
from database.pessoa import Pessoa
from exceptions import (BancoDeDadosError, PessoaJaCadastradaError)


def main():
    pessoa_dao = PessoaDAO()
    pessoa_service = PessoaService(pessoa_dao)
    try:
        criar_tabela()
    except BancoDeDadosError:
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
                try:
                    mostrar_cadastros(pessoa_service.listar())
                except BancoDeDadosError:
                    formatar_erro("Não foi possível acessar o banco de dados.")
            case 2:
                titulo("NOVO CADASTRO")
                pessoa = Pessoa(id=0, nome=ler_nome(), idade=ler_idade())
                try:
                    pessoa_cadastrada = pessoa_service.cadastrar(pessoa)
                    mensagem_cadastro_realizado(pessoa_cadastrada.nome)
                except PessoaJaCadastradaError:
                    formatar_erro("Esse nome já foi cadastrado.")
                except BancoDeDadosError:
                    formatar_erro("Não foi possível acessar o banco de dados.")
            case 3:
                titulo("BUSCAR CADASTRO")
                id_pessoa = ler_id()
                try:
                    dado = pessoa_service.buscar(id_pessoa)
                    if dado is None:
                        formatar_erro("Não existe nenhuma pessoa cadastrada com esse ID!")
                    else:
                        mostrar_cadastro_unico(dado)
                except BancoDeDadosError:
                    formatar_erro("Não foi possível acessar o banco de dados.")
            case 4:
                titulo("ATUALIZAR CADASTRO")
                id_pessoa = ler_id()
                try:
                    pessoa_econtrada = pessoa_service.buscar(id_pessoa)
                    if pessoa_econtrada is None:
                        formatar_erro("Não existe nenhuma pessoa cadastrada com esse ID!")
                    else:
                        pessoa_econtrada.nome = ler_nome()
                        pessoa_econtrada.idade = ler_idade()
                        if pessoa_service.atualizar(pessoa_econtrada):
                            mensagem_alteracao_realizada(pessoa_econtrada.nome, pessoa_econtrada.idade)
                        else:
                            formatar_erro("Não foi possível alterar os dados dessa pessoa. Tente novamente mais tarde!")
                except BancoDeDadosError:
                    formatar_erro("Não foi possível acessar o banco de dados.")
            case 5:
                titulo("EXCLUIR CADASTRO")
                id_pessoa = ler_id()
                try:
                    if pessoa_service.excluir(id_pessoa):
                        mensagem_exclusao_realizada()
                    else:
                        formatar_erro("Não foi possível excluir esse registro. Tente novamente mais tarde!")
                except BancoDeDadosError:
                    formatar_erro("Não foi possível acessar o banco de dados.")
        linha()
        retornar()

if __name__ == "__main__":
    main()
            