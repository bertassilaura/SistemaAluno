from limite.tela_abstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):

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
                if inteiros_possiveis:
                    print("Inteiros possíveis: ", inteiros_possiveis)

    def tela_opcoes(self):
        print("***** BEM-VINDO AO SEU SISTEMA DE ORGANIZAÇÃO :) *****")
        print("Para onde você quer ir? Escolha uma opção:")
        print("1 - Aluno")
        print("2 - Professor")
        print("3 - Matéria")
        print("4 - Tarefa")
        print("0 - Encerrar sistema")
        
        opcao = self.le_numero_inteiro("Digite a opção escolhida: ", [1,2,3,4,0])
        return opcao

    def mostra_mensagem(self):
        pass

    def mostra_dados(self):
        pass

    def pega_dados(self):
        pass