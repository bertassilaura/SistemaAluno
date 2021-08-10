from limite.tela_abstrata import TelaAbstrata
from controlador.controlador_professor import ControladorProfessor

class TelaMateria(TelaAbstrata):

    # Fazer tratamento de dados na recpçao de dados para a opcao
    def tela_opcoes():
        print("***** Você está na página Matéria! *****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar Matéria")
        print("2 - Excluir Matéria")
        print("3 - Listar as matérias do semestre")
        print("4 - Listar as matérias por professor")
        print("5 - Listar as matérias por semana")
        print("6 - Calcular média final de uma matéria")
        print("7 - Ver matérias")
        print("0 - Retornar")

        opcao = int(input("Digite a opção escolhida:"))
        return opcao

    # Fazer tratamento de dados
    def pega_dados(self):
        print("**** DADOS DA MATERIA ****")
        print("Insira os dados")
        nome = str(input("Nome: "))
        semestre = str(input("Semestre:"))
        codigo = str(input("Codigo: "))
        dia_da_semana = str(input("Dia da semana: "))
        horario = str(input("Horario: "))
        link = str(input("Link: "))
        classificacao = str(input("Classificacao: "))
        criterio_de_presenca = str(input("Criterio de presenca:"))
        numero_avaliacoes = str(input("Numero de avaliacoes: "))
        
        dados_materia = {"nome": nome, "semestre": semestre, "codigo": codigo, "dia_da_semana": dia_da_semana,
                        "horario": horario, "link": link, "classificacao": classificacao,
                        "criterio_de_presenca": criterio_de_presenca, "numero_avaliacoes": numero_avaliacoes}
        return dados_materia
    
    def mostra_dados(self, dados_materia):
        print("**** DADOS DO ALUNO ****")
        print("NOME DA MATÉRIA: ", dados_materia['nome'])
        print("PROFESSOR QUE MINISTRA: ", dados_materia['professor'])
        print("SEMESTRE: ", dados_materia['semestre'])
        print("CODIGO DA MATERIA: ", dados_materia['codigo'])
        print("DIA DA SEMANA: ", dados_materia['dia_da_semana'])
        print("HORARIO: ", dados_materia['horario'])
        print("LINK: ", dados_materia['link'])
        print("CLASSIFICACAO: ", dados_materia['classificacao'])
        print("CRITERIO DE PRESENCA: ", dados_materia['criterio_de_presenca'])
        print("NUMERO AVALIACOES: ", dados_materia['numero_avaliacoes'])
        print('\n')
    
    # Fazer tratamento de dados
    def selecionar_materia(self):
        nome = str(input("Nome da materia que deseja selecionar: "))
        return nome
    
    def mostra_mensagem(self, msg):
        print(msg)