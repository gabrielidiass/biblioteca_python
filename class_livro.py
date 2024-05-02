class Livro:
    def __init__(self, titulo, autor, ano_publicacao, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.num_copias = num_copias



    def emprestar_livro(self):
        if self.num_copias > 0:
            self.num_copias -= 1
            print(f"Livro {self.titulo} emprestado com sucesso!")
        else:
            print("Desculpe, este livro não está disponível para empréstimo.")

    def devolver_livro(self):
        self.num_copias += 1
        print(f"Livro {self.titulo} devolvido com sucesso!")
