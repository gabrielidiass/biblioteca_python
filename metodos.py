
from class_biblioteca import Biblioteca
from class_livro import Livro
from class_usuario import Usuario

biblioteca = Biblioteca()


def adicionar_livros_pessoas():
    livro1 = Livro("Python para Iniciantes", "John Doe", 2020, 1)
    livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1)
    livro3 = Livro("Cidades de papel", "John Green", 2016, 1)
    usuario1 = Usuario("Gabrieli", 111000, 91227499)
    usuario2 = Usuario("Roberta", 222000, 91227499)
    
    # Adicionando os livros à biblioteca
    biblioteca.cadastrar_livro(livro1)
    biblioteca.cadastrar_livro(livro2)
    biblioteca.cadastrar_livro(livro3)
    biblioteca.cadastrar_usuario(usuario1)
    biblioteca.cadastrar_usuario(usuario2)
def emprestar_livro():
    titulo = input("Digite o titulo do livro ")
    identificacao = int(input("Digite o cpf do usuário "))
    biblioteca.emprestar_livro(titulo, identificacao)
   
def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    ano = input("Digite o ano de publicação: ")
    num_copias = int(input("Digite o número de cópias disponíveis: "))

    novo_livro = Livro(titulo, autor, ano, num_copias)
    biblioteca.cadastrar_livro(novo_livro)
    print("Livro cadastrado com sucesso!") 
    
def devolver_livro():
    titulo = input("Digite o título do livro: ")
    usuario = input("Digite o cpf do usuário: ")
    biblioteca.devolver_livro(titulo,usuario)

def consultar_livro():
    
    text = """
    Consultar disponibilidade do livro por:
    1. Nome
    2. Autor
    3. Ano de publicação
    """
    print(text)
    choice = int(input())

    if 0 < choice < 4:
        if choice == 1:
            titulo = input("Digite o nome do livro")
            biblioteca.consultar_livros_por_titulo(titulo)
        if choice == 2:
            autor = input("Digite o nome do autor do livro")
            biblioteca.consultar_livros_por_autor(autor)
        if choice == 3:
            ano = input("Digite o ano de publicação do livro")
            biblioteca.consultar_livros_por_ano(ano)
            
def cadastrar_usuario():
    nome = input("Digite o nome do usuario: ")
    identificacao = input("Digite o cpf do usuário sem espaços ou caracteres especiais: ")
    contato = input("Digite o contato do usuário sem espaços ou caracteres especiais: ")
 
    novo_usuario = Usuario(nome, identificacao, contato)
    biblioteca.cadastrar_usuario(novo_usuario)
    print("Usuario cadastrado com sucesso!") 

