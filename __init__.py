from class_biblioteca import Biblioteca
from class_livro import Livro
from class_usuario import Pessoa
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
        if menu_livros_choice == 2:
           biblioteca.gerar_relatorio_livros()
        if menu_livros_choice == 3:
            devolver_livro()
        if menu_livros_choice == 4:
            emprestar_livro()
        if menu_livros_choice == 5:
            consultar_livro()

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
        if choice == 2:
           biblioteca.gerar_relatorio_usuarios()
        
    
    
main()