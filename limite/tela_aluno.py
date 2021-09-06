from limite.tela_abstrata import TelaAbstrata

class TelaAluno(TelaAbstrata):

    def le_numero_inteiro(self, mensagem: str = "", inteiros_possiveis: list() = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_possiveis and inteiro not in inteiros_possiveis:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor não existente: Digite um valor contido nas opções")
                print("\n")
                if inteiros_possiveis:
                    print("Inteiros possíveis: ", inteiros_possiveis)
                    print("\n")

    def tela_opcoes(self):
        print("**** Você está na página Aluno! ****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Criar aluno")
        print("2 - Mostrar aluno")
        print("3 - Alterar Aluno")
        print("0 - Retornar")
        
        opcao = self.le_numero_inteiro("Digite a opção escolhida: ", [1,2,3,0])
        print("\n")
        return opcao
    
    def pega_dados(self):
        print("**** RECEBENDO DADOS DO ALUNO ****")
        print("Insira os dados:")
        nome = str(input("Nome: "))
        email = str(input("Email: "))
        matricula = str(input("Matrícula: "))

        dados_aluno = {"nome": nome, "email": email, "matricula": matricula}
        return dados_aluno

    def mostra_dados(self, dados_aluno):
        print("**** DADOS DO AUNO ****")
        print("Nome do aluno: ", dados_aluno["nome"])
        print("Email do aluno: ", dados_aluno["email"])
        print("Matricula do aluno: ", dados_aluno["matricula"])
        print('\n')

    def mostra_mensagem(self, msg):
        print(msg)
