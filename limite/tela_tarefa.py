from limite.tela_abstrata import TelaAbstrata

class TelaTarefa(TelaAbstrata):
    
    # Fazer tratamento de dados na recpçao de dados na opcao
    def tela_opcoes(self):
        print("**** Você está na página Tarefa! ****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar tarefa")
        print("2 - Excluir tarefa")
        print("3 - Listar tarefas")
        print("4 - Listar tarefas feitas")
        print("5 - Listar tarefas a fazer")
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
        materia_correspondente = str(input("Digite o código da matéria correspondente: "))
        status_realizado = str(input("Está feita ou não?: "))
        peso = int(input("Peso: "))
        nota = str(input("Nota: "))

        dados_tarefa = {"nome_tarefa": nome_tarefa, "data_prazo": data_prazo, "horario_prazo": horario_prazo, "descricao": descricao, "materia_correspondente": materia_correspondente, "status_realizado": status_realizado, "peso": peso, "nota": nota}
        return dados_tarefa

    def mostra_dados(self, dados_tarefa):
        print("NOME DA TAREFA: ", dados_tarefa["Nome da tarefa"])
        print("DATA DO PRAZO ", dados_tarefa["Data do prazo"])
        print("HORÁRIO DO PRAZO: ", dados_tarefa["Horario do prazo"])
        print("DESCRICAO: ", dados_tarefa["Descricao"])
        print("MATERIA CORRESPONDENTE: ", dados_tarefa["Materia correspondente"])
        print("STATUS DE REALIZAÇÃO: ", dados_tarefa["Status de realizacao"])
        print("NOTA ", dados_tarefa["Nota"])
        
    def seleciona_tarefa(self):
        nome = str(input("Nome da tarefa que deseja selecionar: "))
        return nome

    def mostra_mensagem(self, msg):
        print(msg)
