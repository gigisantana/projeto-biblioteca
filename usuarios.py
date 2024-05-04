from sinalizacaoErros import SinalizacaoErros

class Usuario:
    def __init__(self, nome, id_usuario, telefone):
        self.nome = nome
        self.id_usuario = id_usuario
        self.telefone = telefone

class GerenciarUsuarios:
    def __init__(self):
        self.usuarios = []
    
    def adicionar_usuario(self, usuario):
        id_usuario = input("Digite um ID (XXX): ")
        nome = input("Informe o nome do usuário: ")
        telefone = input("Informe um telefone (XXXXXXXXX): ")
        self.verificar_usuario(id_usuario, nome, telefone)

    def verificar_usuario(self, id_usuario, nome, telefone):
        if len(id_usuario) != 3:
            SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro9)
            return
        if not id_usuario.isdigit():
            SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro9)
            return
        if len(telefone) != 9:
            SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro11)
            return
        for caractere in nome:
            if not caractere.isalpha() and not caractere.isspace():
                SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro10)
                return
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                print("Esse id já está sendo usado. tente outro!")
                return

    
    def mostrar_usuarios(self):
        if self.usuarios:
            print("-- Usuarios Cadastrados --")
            for usuario in self.usuarios:
                print(f"Id: {usuario.id}, Nome: {usuario.nome}, Telefone: {usuario.telefone}")
        else:
            SinalizacaoErros.sinalizar_erro(SinalizacaoErros.erro3)
            return
