from limite.tela_abstrata import TelaAbstrata

class TelaAluno(TelaAbstrata):

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
        matricula = int(input("Matrícula: "))

        return {"nome":nome, "email":email, "matricula": matricula}

    def mostra_dados(self, dados_aluno):
        print("**** DADOS DO AUNO ****")
        print("Nome do aluno: ", dados_aluno["nome"])
        print("Email do aluno", dados_aluno["email"])
        print("Matricula do aluno", dados_aluno["matricula"])
        print('\n')

    def le_num_inteiro():
        pass
    
    def mostra_mensagem():
        pass