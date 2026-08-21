from interface import (mostrar_menu, pedir_opcao, sair, linha, retornar, titulo, ler_nome, ler_idade, ler_id, mostrar_cadastros, mensagem_cadastro_realizado, formatar_erro, mensagem_alteracao_realizada, mensagem_exclusao_realizada, mensagem_sem_cadastros, mostrar_cadastro_unico)
from database import criar_tabela
from database import PessoaDAO
from services import PessoaService
from domain import Pessoa
from exceptions import (BancoDeDadosError, PessoaJaCadastradaError, NomeInvalidoError, NomeIncompletoError, NomeComCaracteresInvalidosError, IdadeInvalidaError)

def main():
    pessoa_repository = PessoaDAO()
    pessoa_service = PessoaService(pessoa_repository)
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
                    lista = pessoa_service.listar()
                    if not lista:
                        mensagem_sem_cadastros()
                    else:
                        mostrar_cadastros(lista)
                except BancoDeDadosError:
                    formatar_erro("Não foi possível acessar o banco de dados.")
            case 2:
                titulo("NOVO CADASTRO")
                try:
                    pessoa = Pessoa(id=None, nome=ler_nome(), idade=ler_idade())
                    id_gerado = pessoa_service.cadastrar(pessoa)
                    pessoa.registrar_persistencia(id_gerado)
                    mensagem_cadastro_realizado(pessoa.nome)
                except NomeIncompletoError:
                    formatar_erro("O nome informado está incompleto.")
                except NomeComCaracteresInvalidosError:
                    formatar_erro("O nome informado possui caracteres inválidos.")
                except NomeInvalidoError:
                    formatar_erro("O nome informado é inválido.")
                except IdadeInvalidaError:
                    formatar_erro("A idade informada é inválida")
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
                    pessoa_encontrada = pessoa_service.buscar(id_pessoa)
                    if pessoa_encontrada is None:
                        formatar_erro("Não existe nenhuma pessoa cadastrada com esse ID!")
                    else:
                        nome_novo = ler_nome()
                        idade_nova = ler_idade()
                        pessoa_service.atualizar(pessoa_encontrada, nome_novo, idade_nova)
                        mensagem_alteracao_realizada(pessoa_encontrada.nome, pessoa_encontrada.idade)
                except NomeIncompletoError:
                    formatar_erro("O nome informado está incompleto.")
                except NomeComCaracteresInvalidosError:
                    formatar_erro("O nome informado possui caracteres inválidos.")
                except NomeInvalidoError:
                    formatar_erro("O nome informado é inválido.")
                except IdadeInvalidaError:
                    formatar_erro("A idade informada é inválida.")
                except PessoaJaCadastradaError:
                    formatar_erro("Esse nome já pertence a outra pessoa.")
                except BancoDeDadosError:
                    formatar_erro("Não foi possível acessar o banco de dados.")
            case 5:
                titulo("EXCLUIR CADASTRO")
                id_pessoa = ler_id()
                try:
                    if pessoa_service.excluir(id_pessoa):
                        mensagem_exclusao_realizada()
                    else:
                        formatar_erro("Não existe nenhuma pessoa cadastrada com esse ID!")
                except BancoDeDadosError:
                    formatar_erro("Não foi possível acessar o banco de dados.")
        linha()
        retornar()

if __name__ == "__main__":
    main()
            