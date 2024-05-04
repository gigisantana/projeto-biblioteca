from livros import RegistroLivros 
from usuarios import GerenciarUsuarios
from sinalizacaoErros import SinalizacaoErros
import sys

class Menu:
    def __init__(self):
        pass

    def menu_principal(self):
        print("-- Menu principal --")
        print(" 1 - Pesquisar livro.")
        print(" 2 - Visualizar.")
        print(" 3 - Emprestar livro.")
        print(" 4 - Devolver livro.")
        print(" 5 - Cadastrar livro.")
        print(" 6 - Cadastrar usuário.")
        print(" 0 - Sair")


    def menu_visualizar(self):
        print("-- Menu de Visualização --")
        print(" 1 - Visualizar livros cadastrados.")
        print(" 2 - Visualizar livros disponíveis.")
        print(" 3 - Visualizar livros emprestados.")
        print(" 4 - Visualizar usuários cadastrados.")
        print(" 0 - Retornar ao menu principal")
    
    def executar(self):
        registro = RegistroLivros()

        while True:
            self.menu_principal()
            opcao = input("Escolha a opção desejada: ")
            if opcao == "1":
                opcao_pesquisa = input("Digite a opção de pesquisa (1 - Título, 2 - Autor, 3- Ano de Publicação): ")
                resultados = []
                if opcao_pesquisa == "1":
                    termo = input("Digite o título do livro: ")
                    resultados = RegistroLivros.pesquisar_titulo(termo)
                elif opcao_pesquisa == "2":
                    termo = input("Digite o nome do autor: ")
                    resultados = RegistroLivros.pesquisar_autor(termo)
                elif opcao_pesquisa == "3":
                    termo = input("Digite o ano de publicação: ")
                    resultados = RegistroLivros.pesquisar_ano(termo)
                else:
                    SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro8)
                    return
            elif opcao == "2":
                self.menu_visualizar()
                opcao_visualizar = input("Escolha a opção desejada: ")
                if opcao_visualizar == "1":
                    registro.mostrar_livros_cadastrados()
                
                elif opcao_visualizar == "2":
                    registro.mostrar_livros_disponiveis()
                    
                elif opcao_visualizar == "3":
                    registro.mostrar_livros_emprestados()
                    
                elif opcao_visualizar == "4":
                    GerenciarUsuarios.mostrar_usuarios()
                    
                elif opcao_visualizar == "0":
                    self.menu_principal()

            elif opcao == "3":
                registro.emprestar_livros()
                
            elif opcao == "4":
                registro.devolver_livros()
                
            elif opcao == "5":
                registro.add_livro()
            elif opcao == "6":
                GerenciarUsuarios.adicionar_usuario()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro8)
                return

menu = Menu()
menu.executar()