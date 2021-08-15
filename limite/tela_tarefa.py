from limite.tela_abstrata import TelaAbstrata

class TelaTarefa(TelaAbstrata):

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
        print("**** Você está na página Tarefa! ****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar tarefa")
        print("2 - Excluir tarefa")
        print("3 - Listar tarefas")
        print("4 - Listar tarefas feitas")
        print("5 - Listar tarefas a fazer")
        print("6 - Alterar Tarefa")
        print("0 - Retornar")
        
        opcao = self.le_numero_inteiro("Digite a opção escolhida: ", [1,2,3,4,5,6,0])
        return opcao

    def pega_dados(self):
        print("**** RECEBENDO DADOS DA TAREFA ****")
        print("Insira os dados:")
        nome_tarefa = str(input("Nome: "))
        data_prazo = str(input("Data prazo para entrega: "))
        horario_prazo = str(input("Horário prazo para entrega: ")) 
        descricao = str(input("Descrição resumida da tarefa: "))
        materia_correspondente = str(input("Digite o código da matéria correspondente. Se ainda não criou a materia, ou essa tarefa nao possui materia, deixe em branco: "))
        
        # Recebendo Status
        while True:
            status_realizado = input("Está feita ou não? [sim/nao]: ")
            try:
                status_realizado = str(status_realizado)
                if status_realizado != 'sim' or status_realizado != 'nao':
                    raise ValueError
            except ValueError:
                print("Status inválido: Escreva ''sim'', para feita, ou ''nao'', para não feita.")
            if status_realizado == 'sim' or status_realizado == 'nao':
                break

       # Recebendo Peso
        while True:
            peso = input("Peso: ")
            try:
                peso = float(peso)
                if type(peso) != float:
                    raise ValueError
            except ValueError:
                print("Valor inválido: Insira uma valor numérico, inteiro ou decimal !!")
            if type(peso) == float:
                break

        # Recebendo Nota    
        while True:
            nota = input("Nota: ")
            try:
                nota = float(nota)
                if type(nota) != float:
                    raise ValueError
            except ValueError:
                print("Valor inválido: Insira uma valor numérico, inteiro ou decimal !!")
            if type(nota) == float:
                break

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
        
    def seleciona_tarefa(self):
        nome = str(input("Nome da tarefa que deseja selecionar: "))
        return nome

    def mostra_mensagem(self, msg):
        print(msg)
