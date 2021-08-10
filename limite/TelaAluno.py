from limite.TelaAbstrata import TelaAbstrata

class TelaAluno(TelaAbstrata):
    def __init__(self, controlador_aluno):
        self.__controlador_aluno = controlador_aluno

    # Fazer tratamento de dados na recpçao de dados na opcao
    def tela_opcoes(self):
        print("**** Você está na página Aluno! ****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Criar aluno")
        print("2 - Mostrar aluno")
        print("0 - Retornar")
        
        opcao = int(input("Digite a opção escolhida: "))
        return opcao
    
    # Fazer tratamento de dados aqui
    def pega_dados(self):
        print("**** RECEBENDO DADOS DO ALUNO ****")
        print("Insira os dados:")
        nome = str(input("Nome: "))
        email = str(input("Email: "))
        matricula = str(input("Matrícula: "))

        dados_aluno = {"nome":nome, "email":email, "matricula": matricula}
        return dados_aluno

    def mostra_dados(self, dados_aluno):
        print("**** DADOS DO AUNO ****")
        print("Nome do aluno: ", dados_aluno["nome"])
        print("Email do aluno", dados_aluno["email"])
        print("Matricula do aluno", dados_aluno["matrícula"])
        print('\n')

    #def verifica_valor()
    #def verifica_dados()