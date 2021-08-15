from limite.tela_abstrata import TelaAbstrata

class TelaTarefa(TelaAbstrata):
    
    def tela_opcoes(self):
        print("**** Você está na página Tarefa! ****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar tarefa")
        print("2 - Excluir tarefa")
        print("3 - Listar todas as tarefas")
        print("4 - Listar tarefas feitas")
        print("5 - Listar tarefas a fazer")
        print("6 - Alterar Tarefa")
        print("0 - Retornar")
        
        opcao = int(input("Digite a opção escolhida: "))
        print("\n")
        return opcao

    def pega_dados(self):
        print("**** RECEBENDO DADOS DA TAREFA ****")
        print("Insira os dados:")
        nome_tarefa = str(input("Nome: "))
        data_prazo = str(input("Data prazo para entrega: "))
        horario_prazo = str(input("Horário prazo para entrega: ")) 
        descricao = str(input("Descrição resumida da tarefa: "))
        materia_correspondente = str(input("Digite o código da matéria correspondente. Se não houver, deixe em branco: "))
        status_realizado = str(input("Está feita ou não? [sim/nao]: "))
       
        peso = input("Peso: ")
        try:
            peso = float(peso)
        except:
            raise ValueError

        nota = input("Nota: ")
        try:
            nota = float(nota)
        except:
            raise ValueError

        dados_tarefa = {"nome_tarefa": nome_tarefa, "data_prazo": data_prazo, "horario_prazo": horario_prazo, "descricao": descricao, "materia_correspondente": materia_correspondente, "status_realizado": status_realizado, "peso": peso, "nota": nota}
        return dados_tarefa

    def mostra_dados(self, dados_tarefa):
        print("NOME DA TAREFA: ", dados_tarefa["nome_tarefa"])
        print("DATA DO PRAZO ", dados_tarefa["data_prazo"])
        print("HORÁRIO DO PRAZO: ", dados_tarefa["horario_prazo"])
        print("DESCRICAO: ", dados_tarefa["descricao"])
        print("MATERIA CORRESPONDENTE: ", dados_tarefa["materia_correspondente"])
        print("STATUS DE REALIZAÇÃO: ", dados_tarefa["status_realizado"])
        print("PESO: ", dados_tarefa["peso"])
        print("NOTA: ", dados_tarefa["nota"])
        print("\n")
        
    def seleciona_tarefa(self):
        nome = str(input("Nome da tarefa que deseja selecionar: "))
        return nome

    def mostra_mensagem(self, msg):
        print(msg)
