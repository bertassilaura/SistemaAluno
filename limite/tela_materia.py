from limite.tela_abstrata import TelaAbstrata
from controlador.controlador_professor import ControladorProfessor
import PySimpleGUI as sg 

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

        layout  = [
            [sg.Text('Matéria')],
            [sg.Button('Adicionar Matéria', key=1)],
            [sg.Button('Excluir Matéria', key=2)],
            [sg.Button('Listar as matérias do semestre', key=3)],
            [sg.Button('Calcular média final de uma matéria', key=4)],
            [sg.Button('Ver matérias', key=5)],
            [sg.Button('Alterar Materia', key=6)],
            [sg.Button('Listar por dia da semana', key=7)],
            [sg.Exit('Retornar', key=0)]
        ]

        window = sg.Window('Tela Matéria').Layout(layout)
        button, values = window.Read()
        window.close()
        return button

    def pega_dados(self):
        
        layout = [
            [sg.Text('Insira os dados')],
            [sg.Text('Nome'), sg.InputText('', key = 'nome')],
            [sg.Text('Semestre (ex: 21.1)'), sg.InputText('', key = 'semestre')],
            [sg.Text('ID do professor responsável; Se não houver, deixe em branco'), sg.InputText('', key = 'professor')],
            [sg.Text('Codigo'), sg.InputText('', key = 'codigo')],
            [sg.Text('Horario'), sg.InputText('', key = 'horario')],
            [sg.Text('Link'), sg.InputText('', key = 'link')],
            [sg.Text('Classificacao'), sg.InputCombo(('Assincrona', 'Sincrona'),key = 'classificacao')],
            [sg.Text('Criterio de presenca'), sg.InputText('', key = 'criterio_de_presenca')],
            [sg.Text('Numero de avaliacoes'), sg.Spin([i for i in range(0,101)], initial_value='selecione', key = 'numero_avaliacoes')],
            [sg.Text('Dia da semana'), sg.InputCombo(('Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta'), key = 'dia_da_semana')],
            [sg.Submit('Confirmar'), sg.Cancel('Retornar')]
        ]

        window = sg.Window('Dados da matéria').Layout(layout)
        button, dados_materia = window.Read()
        window.close()
        if button == 'Confirmar':
            return dados_materia

    
    def mostra_dados(self, dados_materia):

        materias = [
            [sg.Text('Materia')],
            [sg.Listbox(values=dados_materia.values(), size=(30,6))],
            [sg.Text('')]
        ]

        layout = [
            [sg.Text('Listando matérias')],
            [materias],
            [sg.Text('')],
            [sg.Cancel('Retornar')]

        ]

        window = sg.Window('Lista de matérias').Layout(layout)
        button, values = window.Read()
        window.close()
        return values

        '''print("**** DADOS DA MATERIA ****")
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
        print('\n')'''

    def selecionar_materia(self):
        codigo = str(input("Código da materia que deseja selecionar: "))
        codigo = codigo.upper()
        print("\n")
        return codigo
    
    def mostra_mensagem(self, msg):
        print(msg)
