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
        status_realizado = str(input("Está feita ou não?: "))
        nota = str(input("Nota: "))

        dados_tarefa = {"Nome da tarefa": nome_tarefa, "Data do prazo": data_prazo, "Horario do prazo": horario_prazo, "Descricao": descricao, "Materia correspondente": materia_correspondente, "Status de realizacao": status_realizado, "Nota": nota}
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
