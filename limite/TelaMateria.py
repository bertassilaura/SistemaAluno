from limite.TelaAbstrata import TelaAbstrata


class TelaMateria(TelaAbstrata):

    def tela_opcoes():
        print("***** Você está na página Matéria! *****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar Matéria")
        print("2 - Excluir Matéria")
        print("3 - Listar as matérias do semestre")
        print("4 - Listar as matérias por professor")
        print("5 - Listar as matérias por dia específico")
        print("6 - Listar as matérias da semana")
        print("7 - Calcular média final de uma matéria")
        print("8 - Ver dados de uma matéria")
        print("0 - Retornar")

        opcao = int(input("Digite a opção escolhida:"))
        return opcao
