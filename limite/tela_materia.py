from limite.tela_abstrata import TelaAbstrata
from controlador.controlador_professor import ControladorProfessor

class TelaMateria(TelaAbstrata):

    def tela_opcoes(self):
        print("***** Você está na página Matéria! *****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar Matéria")
        print("2 - Excluir Matéria")
        print("3 - Listar Matérias por semestre")
        print("4 - Calcular média final de uma matéria")
        print("5 - Ver todas as Matérias")
        print("6 - Alterar Matéria")
        print("0 - Retornar")

        opcao = int(input("Digite a opção escolhida: "))
        print("\n")
        return opcao

    def pega_dados(self):
        print("**** DADOS DA MATERIA ****")
        print("Insira os dados")
        nome = str(input("Nome: "))
        semestre = str(input("Semestre (ex: 21.1): "))
        professor = str(input("Nome do professor responsável; Se não houver, deixe em branco: "))
        codigo = str(input("Código: "))
        dia_da_semana = str(input("Dia da semana [seg/ter/qua/qui/sex]: "))
        horario = str(input("Horário: "))
        link = str(input("Link: "))
        classificacao = str(input("Classificação [assincrona/sincrona]: "))
        criterio_de_presenca = str(input("Critério de presença: "))
        numero_avaliacoes = str(input("Número de avaliações: "))
        
        dados_materia = {"nome": nome, "semestre": semestre, "professor": professor, "codigo": codigo, "dia_da_semana": dia_da_semana,
                        "horario": horario, "link": link, "classificacao": classificacao,
                        "criterio_de_presenca": criterio_de_presenca, "numero_avaliacoes": numero_avaliacoes}
        return dados_materia
    
    def mostra_dados(self, dados_materia):
        print("**** DADOS DA MATERIA ****")
        print("NOME DA MATÉRIA: ", dados_materia['nome'])
        print("PROFESSOR QUE MINISTRA: ", dados_materia['professor'])
        print("SEMESTRE: ", dados_materia['semestre'])
        print("CÓDIGO DA MATÉRIA: ", dados_materia['codigo'])
        print("DIA DA SEMANA: ", dados_materia['dia_da_semana'])
        print("HORÁRIO: ", dados_materia['horario'])
        print("LINK: ", dados_materia['link'])
        print("CLASSIFICAÇÃO: ", dados_materia['classificacao'])
        print("CRITÉRIO DE PRESENÇA: ", dados_materia['criterio_de_presenca'])
        print("NÚMERO DE AVALIAÇÕES: ", dados_materia['numero_avaliacoes'])
        print('\n')

    def selecionar_materia(self):
        nome = str(input("Código da matéria que deseja selecionar: "))
        return nome
    
    def mostra_mensagem(self, msg):
        print(msg)
