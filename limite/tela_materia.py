from limite.tela_abstrata import TelaAbstrata

class TelaMateria(TelaAbstrata):

    def tela_opcoes(self):
        print("***** Você está na página Matéria! *****")
        print("O que você deseja fazer? Escolha uma opção:")
        print("1 - Adicionar Matéria")
        print("2 - Excluir Matéria")
        print("3 - Listar as matérias do semestre")
        print("4 - Calcular média final de uma matéria")
        print("5 - Ver matérias")
        print("6 - Alterar Materia")
        print("0 - Retornar")

        opcao = int(input("Digite a opção escolhida:"))
        return opcao

    def pega_dados(self):
        print("**** DADOS DA MATERIA ****")
        print("Insira os dados")
        nome = str(input("Nome: "))
        semestre = str(input("Semestre (ex: 21.1):"))
        professor = str(input("Nome do professor responsável; Se não houver, deixe em branco: "))
        codigo = str(input("Codigo: "))
        dia_da_semana = str(input("Dia da semana [seg/ter/qua/qui/sex]: "))
        horario = str(input("Horario: "))
        link = str(input("Link: "))
        classificacao = str(input("Classificacao [assincrona/sincrona]: "))
        criterio_de_presenca = str(input("Criterio de presenca:"))
        numero_avaliacoes = str(input("Numero de avaliacoes: "))
        
        return {"nome": nome, "semestre": semestre, "codigo": codigo, "dia_da_semana": dia_da_semana,
                        "horario": horario, "link": link, "classificacao": classificacao,
                        "criterio_de_presenca": criterio_de_presenca, "numero_avaliacoes": numero_avaliacoes}
    
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
        nome = str(input("Código da materia que deseja selecionar: "))
        return nome
    
    def mostra_mensagem(self, msg):
        print(msg)
