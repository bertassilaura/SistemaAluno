from limite.TelaAbstrata import TelaAbstrata
from controlador.ControladorProfessor import ControladorProfessor

class TelaProfessor(TelaAbstrata):
    def __init__(self, controlador_professor: ControladorProfessor):
        self.__controlador__professor = controlador_professor

    # Fazer tratamento de dados na recpçao de dados na opcao
    def tela_opcoes(self):
        print("***** Você está na página Professor! *****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar um professor")
        print("2 - Excluir um professor")
        print("3 - Listar Professores")
        print("0 - Retornar")

        opcao = int(input("Digite a opção escolhida: "))
        return opcao

    # Fazer tratamento de dados aqui
    def pega_dados(self):
        print("***** RECEBENDO DADOS DO PROFESSOR *****")
        print("Insira os dados:")
        nome = str(input("Nome: "))
        email = str(input("Email: "))
        telefone = str(input("Telefone: "))

        dados_professor = {"nome": nome, "email": email, "telefone": telefone}
        return dados_professor

   
    def mostra_dados(self, dados_professor):
        print("NOME DO PROFESSOR: ", dados_professor["nome"])
        print("EMAIL DO PROFESSOR: ", dados_professor["email"])
        print("TELEFONE DO PROFESSOR: ", dados_professor["telefone"])
        print("\n")

    # Fazer tratamento de dados aqui
    def selecionar_professor(self):
        nome = str(input("Nome do professor que deseja selecionar: "))
        return nome

    def mostra_mensagem(self, msg):
        print(msg)
