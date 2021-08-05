from limite.TelaAbstrata import TelaAbstrata
from controlador.ControladorTarefa import ControladorTarefa

class TelaTarefa(TelaAbstrata):
    def __init__(self, controlador_tarefa: ControladorTarefa):
        self.__controlador_tarefa = controlador_tarefa

    def tela_opcoes(self):
        print("**** Você está na página Tarefa! ****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar tarefa")
        print("2 - Excluir tarefa")
        print("3 - Listar tarefas")
        print("0 - Retornar")
        
        opcao = int(input("Digite a opção escolhida: "))
        return opcao

    # Fazer tratamento de dados aqui
    def pega_dados(self):
        print("**** RECEBENDO DADOS DA TAREFA ****")
        print("Insira os dados:")
        nome_tarefa = str(input("Nome: "))
        data_prazo = str(input("Data prazo para entrega: ")) # Verificar como receber com o tipo date e no formato correto
        horario_prazo = str(input("Horário prazo para entrega: ")) # Verificar como receber com o tipo time e no formato correto
        descricao = str(input("Descrição resumida da tarefa: "))
        materia_correspondente = str(input("De qual materia?: ")) # Verificar como fazer a relação com a classe Materia
        status_realizado = str(input("Está feita ou não?: "))
        nota = str(input("Nota: "))

        dados_aluno = {"nome":nome, "email":email, "matricula": matricula}
        return dados_aluno
