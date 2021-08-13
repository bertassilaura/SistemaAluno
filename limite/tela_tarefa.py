from limite.tela_abstrata import TelaAbstrata

class TelaTarefa(TelaAbstrata):
        
    # Fazer tratamento de dados na recpçao de dados na opcao
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
        status_realizado = str(input("Responda True, para tarefa feita ou False, para não feita: ")) # Vai receber bool ou str mesmo?
        nota = float(input("Nota: "))

        return {"nome_tarefa":nome_tarefa, "data_prazo":data_prazo, "horario_prazo":horario_prazo,
                "descricao":descricao, "materia_correspondente":materia_correspondente, "status_realizado":status_realizado,
                "nota":nota}

    def selecionar_tarefa(self):
        nome = str(input("Nome da Tarefa que deseja selecionar: "))
        return nome
    
    def mostra_mensagem(self, msg):
        print(msg)

    def le_num_inteiro():
        pass

    def mostra_dados():
        pass
