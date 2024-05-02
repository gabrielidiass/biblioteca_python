class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def emprestar_livro(self, titulo_livro, identificacao_usuario):
        for livro in self.livros:
            if livro.titulo == titulo_livro and livro.num_copias > 0:
                for usuario in self.usuarios:
                    if usuario.identificacao == identificacao_usuario:
                        livro.emprestar_livro()
                        return
                print("Usuário não encontrado.")
                return
        print("Livro não encontrado ou não disponível.")

    def devolver_livro(self, titulo_livro, identificacao_usuario):
        for livro in self.livros:
            if livro.titulo == titulo_livro:
                livro.devolver_livro()
                return
        print("Livro não encontrado.")

    def consultar_livros_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                print(livro.titulo, livro.autor, livro.ano_publicacao, livro.num_copias)

    def consultar_livros_por_autor(self, autor):
        for livro in self.livros:
            if livro.autor.lower() == autor.lower():
                print(livro.titulo, livro.autor, livro.ano_publicacao, livro.num_copias)

    def consultar_livros_por_ano(self, ano):
        for livro in self.livros:
            if livro.ano_publicacao == ano:
                print(livro.titulo, livro.autor, livro.ano_publicacao, livro.num_copias)

    def gerar_relatorio_livros(self):
        print("Relatório de Livros Disponíveis:")
        for livro in self.livros:
            if livro.num_copias > 0:
                print(livro.titulo, livro.autor, livro.ano_publicacao, livro.num_copias)

        print("\nRelatório de Livros Emprestados:")
        for livro in self.livros:
            if livro.num_copias == 0:
                print(livro.titulo, livro.autor, livro.ano_publicacao, livro.num_copias)
                
def gerar_relatorio_usuarios(self):
        print("\nLista de Usuários:")
        for usuario in self.usuarios:
            print(usuario.nome, usuario.identificacao, usuario.contato)
