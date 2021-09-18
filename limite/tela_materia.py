from PySimpleGUI.PySimpleGUI import Sizer
from entidade.materia import Materia
from limite.tela_abstrata import TelaAbstrata
from controlador.controlador_professor import ControladorProfessor
import PySimpleGUI as sg 
from limite.temas import *

class TelaMateria(TelaAbstrata):

    sg.theme(tema)

    def tela_opcoes(self):

        layout  = [
            [sg.Image(logo2, size=(180, 180))],
            [sg.Text('Você está na página Matéria!', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text('O que deseja fazer?', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Button('Adicionar Matéria', font=fonte_texto, size=tamanho_texto, key=1)],
            [sg.Button('Excluir Matéria', font=fonte_texto, size=tamanho_texto, key=2)],
            [sg.Button('Matérias por semestre', font=fonte_texto, size=tamanho_texto, key=3)],
            [sg.Button('Calcular Média final', font=fonte_texto, size=tamanho_texto, key=4)],
            [sg.Button('Ver matérias', font=fonte_texto, size=tamanho_texto, key=5)],
            [sg.Button('Alterar Materia', font=fonte_texto, size=tamanho_texto, key=6)],
            [sg.Button('Listar por dia da semana', font=fonte_texto, size=tamanho_texto, key=7)],
            [sg.Exit('Retornar', font=fonte_texto, size=tamanho_texto, key=8)]
        ]

        window = sg.Window('Matéria', size=(450, 520),  element_justification="c", grab_anywhere=True, default_element_size=(40, 1)).Layout(layout)
        button, values = window.Read()
        window.close()
        return button 

    def pega_dados(self):
        
        layout = [
            [sg.Image(logo2, size=(110,110))],
            [sg.Text('Recebendo dados', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text('Nome', font=fonte_texto, size=tamanho_texto), sg.InputText(key = 'nome')],
            [sg.Text('Semestre (ex: 21.1)', font=fonte_texto, size=tamanho_texto), sg.InputText(key = 'semestre')],
            [sg.Text('ID do professor', font=fonte_texto, size=tamanho_texto), sg.InputText(key = 'professor')],
            [sg.Text('Codigo', font=fonte_texto, size=tamanho_texto), sg.InputText(key = 'codigo')],
            [sg.Text('Horario', font=fonte_texto, size=tamanho_texto), sg.InputText(key = 'horario')],
            [sg.Text('Link', font=fonte_texto, size=tamanho_texto), sg.InputText(key = 'link')],
            [sg.Text('Classificacao', font=fonte_texto, size=tamanho_texto), sg.InputCombo(('Assincrona', 'Sincrona'), default_value='selecione', key = 'classificacao')],
            [sg.Text('Criterio de presenca', font=fonte_texto, size=tamanho_texto), sg.InputText(key = 'criterio_de_presenca')],
            [sg.Text('Numero de avaliacoes', font=fonte_texto, size=tamanho_texto), sg.Spin([i for i in range(0,101)], initial_value='selecione', key = 'numero_avaliacoes')],
            [sg.Text('Dia da semana', font=fonte_texto, size=tamanho_texto), sg.InputCombo(('Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta'), key = 'dia_da_semana')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Cancelar e retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Dados da matéria', grab_anywhere=True).Layout(layout)
        button, dados_materia = window.Read()
        window.close()
        if button == 'Confirmar':
            return dados_materia

    
    def mostra_dados(self, materia: Materia):

        materias = [
            [sg.Text('Nome: {}'.format(materia.nome), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Semestre: {}'.format(materia.semestre), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('ID do professor: {}'.format(materia.professor), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Codigo: {}'.format(materia.codigo), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Horario: {}'.format(materia.horario), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Link: {}'.format(materia.link), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Classificacao: {}'.format(materia.classificacao), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Criterio de presenca: {}'.format(materia.criterio_de_presenca), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Numero de avaliacoes: {}'.format(materia.numero_avaliacoes), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Dia da semana: {}'.format(materia.dia_da_semana), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('')]
        ]

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text('Listando matéria', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [materias],
            [sg.Text('')],
            [sg.Cancel('Retornar', font=fonte_texto, size=tamanho_texto)]

        ]

        window = sg.Window('Matérias', size=(450,580), element_justification="c", grab_anywhere=True).Layout(layout)
        button, values = window.Read()
        window.close()
        return values

    def selecionar_materia(self, materias: list):
        materias = [
            [sg.Listbox(values=materias, font=fonte_texto, size=(60, 8), key='materia')]
        ]

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text('Selecione a Matéria', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [materias],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Cancelar e retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Selecionar materias', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button, materia = window.Read()
        window.close()
        if button == 'Confirmar':
            codigo = (materia['materia'][0].split())[1]
            return codigo
        return
    
    def mostra_mensagem(self, msg):

        layout = [
            [sg.Text(msg, font=fonte_texto, justification='c')],
            [sg.Cancel('Ok', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Aviso!', size=(300,100), element_justification="c", grab_anywhere=True).Layout(layout)
        button, msg = window.Read()
        window.close()
        return msg
    
    def dias_da_semana(self):

        layout = [
            [sg.Text('Dias da semana', font=fonte_texto, size=tamanho_texto)],
            [sg.InputCombo(('Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta'), key = 'dia_da_semana')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Cancelar e retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Dias da semana', grab_anywhere=True).Layout(layout)
        button, values = window.Read()
        values = values['dia_da_semana']
        window.close()
        return values
    
    def semestres(self):

        layout = [
            [sg.Text('Insira o semestre desejado', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.InputText('', size=(15,1), key='semestre')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Cancelar e retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Recebe semestre', grab_anywhere=True).Layout(layout)
        button, semestre = window.Read()
        semestre = semestre['semestre']
        window.close()
        return semestre
    
    def mostra_lista(self, materias: list):
        tarefas = [
            [sg.Listbox(values=materias, font=fonte_texto, size=(60, 8))],
        ]

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text('Listando matéritas', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [tarefas],
            [sg.Text('')],
            [sg.Cancel('Retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Lista de materias', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button, values = window.Read()
        window.close()
        return values