class SinalizacaoErros:
    erro1 = "Livro não encontrado!"
    erro2 = "Livro não disponível para empréstimo no momento!"
    erro3 = "Usuário não cadastrado!"
    erro4 = "Nenhum exemplar foi registrado!"
    erro5 = "O usuário não emprestou esse livro!"
    erro6 = "Nenhum exemplar foi emprestado!"
    erro7 = "Não há livro disponível!"
    erro8 = "Opção inválida!!!"
    erro9 = "ID inválido!!"
    erro10 = "Nome inválido!!"
    erro11 = "Telefone inválido!!"
    
    @staticmethod
    def sinalizar_erro(mensagem):
        print(mensagem)