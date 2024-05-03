from class_biblioteca import Biblioteca
from class_livro import Livro
from class_usuario import Usuario
from metodos import *

def main():
    adicionar_livros_pessoas()
    main_menu = """
    MENU PRINCIPAL
    
    Digite o número correspondente para começar 

    1.Menu de livros
    2.Menu de usuários 
    """
    print(main_menu)
    main_menu_choice = int((input()))
    if 0 < main_menu_choice < 3:
        if main_menu_choice == 1:
            menu_livros()   
        if main_menu_choice == 2:
            menu_usuarios()
    else:
        print("Por favor digite um número válido")
       
def menu_livros():
    
    menu_livros_text = """
    1.Cadastrar um livro
    2.Mostrar os livros
    3.Devolver um livro 
    4.Emprestar um livro
    5.consultar a disponibilidade de um livro 
    """
    print(menu_livros_text)
    menu_livros_choice = int(input())
    
    if 0 < menu_livros_choice < 6:
        if menu_livros_choice == 1:
            cadastrar_livro()
            menu_navegacao()
        if menu_livros_choice == 2:
           limpar()
           biblioteca.gerar_relatorio_livros()
           menu_navegacao()
        if menu_livros_choice == 3:
            devolver_livro()
            menu_navegacao()
        if menu_livros_choice == 4:
            emprestar_livro()
            menu_navegacao()
        if menu_livros_choice == 5:
            consultar_livro()
            menu_navegacao()

def menu_usuarios():
    text = """
    1.Cadastrar um novo usuário
    2.Mostrar os usuarios
    """
    print(text)
    choice = int(input())
    if 0 < choice < 3:
        if choice == 1:
            cadastrar_usuario()
            menu_navegacao()
        if choice == 2:
           biblioteca.gerar_relatorio_usuarios()
           menu_navegacao()
        
def menu_navegacao():
    text = """
    1. Voltar ao menu principal
    2. Encerrar programa
    """    
    print(text)
    choice = int(input())
    
    if choice == 1:
        limpar()
        main()
    if choice == 2:
        exit()
        
def limpar():
    print("\n" * 130)
main()
