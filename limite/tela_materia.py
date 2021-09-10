from limite.tela_abstrata import TelaAbstrata
from controlador.controlador_professor import ControladorProfessor

class TelaMateria(TelaAbstrata):

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
                print("\n")
                if inteiros_possiveis:
                    print("Inteiros possíveis: ", inteiros_possiveis)
                    print("\n")

    def tela_opcoes(self):
        print("***** Você está na página Matéria! *****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar Matéria")
        print("2 - Excluir Matéria")
        print("3 - Listar as matérias do semestre")
        print("4 - Calcular média final de uma matéria")
        print("5 - Ver matérias")
        print("6 - Alterar Materia")
        print("7 - Listar por dia da semana")
        

        opcao = self.le_numero_inteiro("Digite a opção escolhida: ", [1,2,3,4,5,6,7,0])
        print("\n")
        return opcao

    def pega_dados(self):
        print("**** DADOS DA MATERIA ****")
        print("Insira os dados")
        nome = str(input("Nome: "))
        semestre = str(input("Semestre (ex: 21.1): "))
        professor = str(input("ID do professor responsável; Se não houver, deixe em branco: "))
        codigo = str(input("Codigo: "))
        codigo = codigo.upper()
        horario = str(input("Horario: "))
        link = str(input("Link: "))
        classificacao = str(input("Classificacao [assincrona/sincrona]: "))
        criterio_de_presenca = str(input("Criterio de presenca: "))
        numero_avaliacoes = str(input("Numero de avaliacoes: "))

        while True: 
            dia_da_semana = input("Dia da semana [seg/ter/qua/qui/sex]: ")
            dia_da_semana = dia_da_semana.lower()
            print("\n")
            try:
                if dia_da_semana != "seg" and dia_da_semana != "ter" and dia_da_semana != "qua" and dia_da_semana != "qui" and dia_da_semana != "sex":
                    raise ValueError
            except ValueError:
                print("Valor Inválido! Insira apenas os valores disponíveis: seg/ter/qua/qui/sex.")
            if dia_da_semana == "seg" or dia_da_semana == "ter" or dia_da_semana == "qua" or dia_da_semana == "qui" or dia_da_semana == "sex":
                break
         
        dados_materia = {"nome": nome, "semestre": semestre, "professor": professor, "codigo": codigo, "dia_da_semana": dia_da_semana,
                        "horario": horario, "link": link, "classificacao": classificacao,
                        "criterio_de_presenca": criterio_de_presenca, "numero_avaliacoes": numero_avaliacoes}
        return dados_materia
    
    def mostra_dados(self, dados_materia):
        print("**** DADOS DA MATERIA ****")
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

    def selecionar_materia(self):
        codigo = str(input("Código da materia que deseja selecionar: "))
        codigo = codigo.upper()
        print("\n")
        return codigo
    
    def mostra_mensagem(self, msg):
        print(msg)
