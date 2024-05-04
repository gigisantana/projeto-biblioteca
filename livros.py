from sinalizacaoErros import SinalizacaoErros


class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_copias = 0
        self.exemplares_disponiveis = self.numero_copias
        self.exemplares_emprestados = []
    
    def atualizar_numero_copias(self):
        self.numero_copias += 1

    def detalhes_livro(livro):
        return f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}"

    def emprestimo(self, usuario):
        if self.numero_copias > 0:
            self.exemplares_emprestados.append(usuario)
            self.exemplares_disponiveis -= 1
            print(f"Livro emprestado com sucesso. Boa leitura!!")
        else: 
            SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro2)
    
    def devolucao(self, usuario):
        if usuario in self.exemplares_emprestados:
            self.exemplares_emprestados.remove(usuario)
            self.exemplares_disponiveis += 1
            print(f"Livro devolvido com sucesso. Obrigada!")
        else:
            SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro5)

class RegistroLivros:
    def __init__(self):
        self.livros = []
# ARRUMAR ISSO AQUIIIIIIIIIIIIIIIIIIIIIII, PQ NÃO TÁ REGISTRANDO
    def add_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano_publicacao = int(input("Digite o ano de publicação do livro: "))

        livro = Livro(titulo, autor, ano_publicacao)

        for L in self.livros:
            if L.titulo == livro.titulo and L.autor == livro.autor:
                livro.atualizar_numero_copias()
                print(f"Livro resgistrado com sucesso! Número de exemplares: {L.numero_copias}")
                break
        else: 
            self.livros.append(livro)
            livro.atualizar_numero_copias()
            print(f"Livro adicionado com sucesso!!")
            print(livro.detalhes_livro())
            return

    def mostrar_livros_cadastrados(self):
        if self.livros:
            print("Livros registrados:")
            for livro in self.livros:
                print(livro.detalhes_livro())
        else:
            SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro4)
    
    def mostrar_livros_disponiveis(self):
        if self.livros:
            print(" -- Livros disponíveis para empréstimo --")
            for livro in self.livros:
                if livro.exemplares_disponiveis > 0:
                    print(livro.detalhe_livro(livro), "Exemplares disponíveis: {livro.exemplares_disponiveis}")
                else:
                    SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro7)
        else:
            SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro4)
    
    def mostrar_livros_emprestados(self):
        if self.livros:
            print(" -- Livros emprestados --")
            livros_encontrados = False
            for livro in self.livros:
                if livro.exemplares_emprestados:
                    livros_encontrados = True
                    print(livro.detalhe_livro(livro))
            if not livros_encontrados:
                SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro6)     
        else:
            SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro4)

        
    def emprestar_livros(self, titulo, usuario):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.emprestimo()
                return
            elif livro.titulo == titulo and livro.disponivel == False:
                # colocar código de erro para cópia não disponível
                SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro2)
            else:
                # colocar código de erro para livro não encontrado
                SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro1)
    
    def devolver_livros(self, titulo, usuario):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.devolucao(usuario)
                return
            else:
                SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro1)
    
    def pesquisar_titulo(self, termo):
        resultados = []
        for livro in self.livros:
            if termo.lower() in livro.titulo.lower():
                resultados.append(livro)
        return resultados
    
    def pesquisar_autor(self, termo):
        resultados = []
        for livro in self.livros:
            if termo.lower() in livro.autor.lower():
                resultados.append(livro)
        return resultados

    def pesquisar_ano(self, termo):
        resultados = []
        for livro in self.livros:
            if termo in str(livro.ano_publicacao):
                resultados.append(livro)
        return resultados
