from limite.TelaAbstrata import TelaAbstrata

class TelaProfessor(TelaAbstrata):

    def tela_opcoes():
        print("***** Você está na página Professor! *****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar um professor")
        print("2 - Excluir um professor")
        print("0 - Retornar")

        opcao = int(input("Digite a opção escolhida: "))
        return opcao

    def pega_dados():
        print("***** DADOS DO PROFESSOR *****")
        print("Insira os dados:")
        nome = str(input("Nome: "))
        email = str(input("Email: "))
        telefone = str(input("Telefone: "))

        return {"nome": nome, "email": email, "telefone": telefone}

   
        