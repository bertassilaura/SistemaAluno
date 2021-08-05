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
