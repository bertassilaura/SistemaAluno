from limite.tela_abstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):

    def tela_opcoes(self):
        print("***** BEM-VINDO AO SEU SISTEMA DE ORGANIZAÇÃO :) *****")
        print("Para onde você quer ir? Escolha uma opção:")
        print("1 - Aluno")
        print("2 - Professor")
        print("3 - Matéria")
        print("4 - Tarefa")
        
        opcao = int(input("Digite a opção escolhida: "))
        print("\n")
        return opcao

    def mostra_mensagem(self):
        pass

    def mostra_dados(self):
        pass

    def pega_dados(self):
        pass