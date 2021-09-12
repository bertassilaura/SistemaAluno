from entidade.materia import Materia
from limite.tela_abstrata import TelaAbstrata
from controlador.controlador_professor import ControladorProfessor
import PySimpleGUI as sg 

class TelaMateria(TelaAbstrata):

    def le_numero_inteiro():
        pass

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
            [sg.Text('Criterio de presenca'), sg.InputText('',  key = 'criterio_de_presenca')],
            [sg.Text('Numero de avaliacoes'), sg.Spin([i for i in range(0,101)], initial_value='selecione', key = 'numero_avaliacoes')],
            [sg.Text('Dia da semana'), sg.InputCombo(('Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta'), key = 'dia_da_semana')],
            [sg.Submit('Confirmar'), sg.Cancel('Retornar')]
        ]

        window = sg.Window('Dados da matéria').Layout(layout)
        button, dados_materia = window.Read()
        window.close()
        if button == 'Confirmar':
            return dados_materia

    
    def mostra_dados(self, materia: Materia):

        materia = [
            [sg.Text('Nome: {}'.format(materia.nome))],
            [sg.Text('Semestre: {}'.format(materia.semestre))],
            [sg.Text('ID do professor: {}'.format(materia.professor))],
            [sg.Text('Codigo: {}'.format(materia.codigo))],
            [sg.Text('Horario: {}'.format(materia.horario))],
            [sg.Text('Link: {}'.format(materia.link))],
            [sg.Text('Classificacao: {}'.format(materia.classificacao))],
            [sg.Text('Criterio de presenca: {}'.format(materia.criterio_de_presenca))],
            [sg.Text('Numero de avaliacoes: {}'.format(materia.numero_avaliacoes))],
            [sg.Text('Dia da semana: {}'.format(materia.dia_da_semana))],
            [sg.Text('')]
        ]

        layout = [
            [sg.Text('Listando matérias')],
            [materia],
            [sg.Text('')],
            [sg.Cancel('Retornar')]

        ]

        window = sg.Window('Lista de matérias').Layout(layout)
        button, values = window.Read()
        window.close()
        return values

    def selecionar_materia(self):

        layout = [
            [sg.Text('Insira o código da matéria que deseja selecionar')],
            [sg.Text('Código'), sg.InputText('', size=(15,1), key='codigo')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar e retornar')]
        ]

        #codigo = str(input("Código da materia que deseja selecionar: "))
        window = sg.Window('Selecionar materias').Layout(layout)
        button, codigo = window.Read()
        codigo = (codigo['codigo'])#.upper()
        window.close()
        return codigo
    
    def mostra_mensagem(self, msg):

        layout = [
            [sg.Text(msg)],
            [sg.Cancel('Ok')]
        ]

        window = sg.Window('Aviso!').Layout(layout)
        button, msg = window.Read()
        window.close()
        return msg
    
    def dias_da_semana(self):

        layout = [
            [sg.Text('Dias da semana')],
            [sg.InputCombo(('Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta'), key = 'dia_da_semana')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar e retornar')]
        ]

        window = sg.Window('Dias da semana').Layout(layout)
        button, values = window.Read()
        values = values['dia_da_semana']
        window.close()
        return values
    
    def semestres(self):

        layout = [
            [sg.Text('Insira o semestre desejado')],
            [sg.InputText('', size=(15,1), key='semestre')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar e retornar')]
        ]

        window = sg.Window('Semestre').Layout(layout)
        button, semestre = window.Read()
        semestre = semestre['semestre']
        window.close()
        return semestre

        

