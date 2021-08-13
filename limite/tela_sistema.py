from limite.tela_abstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):

    def tela_opcoes(self):
        print("***** BEM-VINDO AO SEU SISTEMA DE ORGANIZAÇÃO :) *****")
        print("Para onde você quer ir? Escolha uma opção:")
        print("1 - Aluno")
        print("2 - Professor")
        print("3 - Matéria")
        print("4 - Tarefa")
        print("0 - Encerra sistema")
        
        opcao = int(input("Digite a opção escolhida: "))
        return opcao
     
    def le_num_inteiro():
        pass

    def pega_dados():
        pass

    def mostra_dados():
        pass
    
    def mostra_mensagem():
        pass