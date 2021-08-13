from limite.tela_abstrata import TelaAbstrata

class TelaMateria(TelaAbstrata):
    
    # Fazer tratamento de dados na recpçao de dados para a opcao
    def tela_opcoes(self):
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

    # Fazer tratamento de dados
    def pega_dados(self):
        print("**** DADOS DA MATERIA ****")
        print("Insira os dados")
        nome = str(input("Nome: "))
        self.__controlador_professor.listar_professores()
        posicao_professor = self.__tela_professor.selecionar_professor()
        professor = str(input("Professor: "))
        semestre = str(input("Semestre:"))
        dia_da_semana = str(input("Dia da semana: "))
        horario = str(input("Horario: "))
        link = str(input("Link: "))
        classificacao = str(input("Classificacao: "))
        criterio_de_presenca = str(input("Criterio de presenca:"))
        numero_avaliacoes = int(input("Numero de avaliacoes: "))
        
        return {"nome": nome, "professor" : professor, "semestre": semestre, "dia_da_semana": dia_da_semana,
                        "horario": horario, "link": link, "classificacao": classificacao,
                        "criterio_de_presenca": criterio_de_presenca, "numero_avaliacoes": numero_avaliacoes}
    
    def mostra_dados(self, dados_materia):
        print("**** DADOS DO ALUNO ****")
        print("NOME DA MATÉRIA: ", dados_materia['nome'])
        print("PROFESSOR QUE MINISTRA: ", dados_materia['professor'])
        print("SEMESTRE", dados_materia['semestre'])
        print("DIA DA SEMANA", dados_materia['dia_da_semana'])
        print("HORARIO", dados_materia['horario'])
        print("LINK", dados_materia['link'])
        print("CLASSIFICACAO", dados_materia['classificacao'])
        print("CRITERIO DE PRESENCA", dados_materia['criterio_de_presenca'])
        print("NUMERO AVALIACOES", dados_materia['numero_avaliacoes'])
        print('\n')
    
    # Fazer tratamento de dados
    def selecionar_materia(self):
        nome = str(input("Nome da materia que deseja selecionar: "))
        return nome
    
    def mostra_mensagem(self, msg):
        print(msg)

    def le_num_inteiro():
        pass
