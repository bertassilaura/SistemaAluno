from limite.tela_abstrata import TelaAbstrata

class TelaProfessor(TelaAbstrata):

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
        print("***** Você está na página Professor! *****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar um professor")
        print("2 - Excluir um professor")
        print("3 - Listar Professores")
        print("4 - Alterar Professor")
        print("0 - Retornar")

        opcao = self.le_numero_inteiro("Digite a opção escolhida: ", [1,2,3,4,0])
        print("\n")
        return opcao

    def pega_dados(self):
        print("***** RECEBENDO DADOS DO PROFESSOR *****")
        print("Insira os dados:")
        nome = str(input("Nome: "))
        email = str(input("Email: "))
        telefone = str(input("Telefone: "))

        dados_professor = {"nome": nome, "email": email, "telefone": telefone}
        return dados_professor
   
    def mostra_dados(self, dados_professor):
        print("Nome do professor: ", dados_professor["nome"])
        print("Email do professor: ", dados_professor["email"])
        print("Telefone do professor: ", dados_professor["telefone"])
        print("ID do professor: ", dados_professor["id_professor"])
        print("\n")

    def selecionar_professor(self):
        nome = str(input("ID do professor que deseja selecionar: "))
        print("\n")
        return nome

    def mostra_mensagem(self, msg):
        print(msg)

