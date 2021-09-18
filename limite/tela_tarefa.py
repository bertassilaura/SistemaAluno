from entidade.tarefa import Tarefa
from PySimpleGUI.PySimpleGUI import InputText
from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from limite.temas import *

class TelaTarefa(TelaAbstrata):

    sg.theme(tema)

    def le_numero_inteiro():
        pass
    
    def tela_opcoes(self):

        layout  = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text('Tarefa', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Button('Adicionar Tarefa', font=fonte_texto, size=tamanho_texto, key=1)],
            [sg.Button('Excluir Tarefa', font=fonte_texto, size=tamanho_texto, key=2)],
            [sg.Button('Listar Tarefas', font=fonte_texto, size=tamanho_texto, key=3)],
            [sg.Button('Listar tarefas feitas', font=fonte_texto, size=tamanho_texto, key=4)],
            [sg.Button('Listar tarefas a fazer', font=fonte_texto, size=tamanho_texto, key=5)],
            [sg.Button('Alterar Tarefa', font=fonte_texto, size=tamanho_texto, key=6)],
            [sg.Exit('Retornar', font=fonte_texto, size=tamanho_texto, key=7)]
        ]

        window = sg.Window('Tela Tarefa', size=tamanho_janela, element_justification="c", grab_anywhere=True, default_element_size=(40, 1)).Layout(layout)
        button, values = window.Read()
        window.close()
        print(button)
        return button

    def pega_dados(self):

        layout = [
            [sg.Image(logo2, size=(110,110))],
            [sg.Text('Recebendo dados de Tarefa', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text('Nome', font=fonte_texto, size=tamanho_texto), sg.InputText('Atribua um nome para a tarefa', key = 'nome_tarefa')],
            [sg.Text('Data prazo', font=fonte_texto, size=tamanho_texto), sg.InputText('DD/MM/AA', key = 'data_prazo')], 
            [sg.Text('Horário prazo', font=fonte_texto, size=tamanho_texto), sg.InputText('00:00', key = 'horario_prazo')],
            [sg.Text('Descrição', font=fonte_texto, size=tamanho_texto), sg.Multiline(default_text= 'Descrição resumida da tarefa', key = 'descricao')],
            [sg.Text('Está feita ou não?', font=fonte_texto, size=tamanho_texto), sg.InputCombo(('sim', 'não'),default_value='selecione', size=(9,1),key = 'status_realizado')],
            [sg.Text('Código da matéria', font=fonte_texto, size=tamanho_texto), sg.InputText('Se não criou a materia, ou nao possui materia, deixe em branco',  key = 'materia_correspondente')],
            [sg.Text('Peso', font=fonte_texto, size=tamanho_texto), sg.InputText('Exemplo: 0.2',  key = 'peso') ], # receber float sg.Spin([i for i in range(0,101)], initial_value='selecione', key = 'peso')
            [sg.Text('Nota', font=fonte_texto, size=tamanho_texto), sg.InputText('Exemplo: 8.5', key = 'nota')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Cancelar e retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Dados da tarefa', grab_anywhere=True).Layout(layout)
        button, dados_tarefa = window.Read()
        window.close()
        if button == 'Confirmar':
            return dados_tarefa

    def mostra_dados(self, tarefa: Tarefa):
        descricao = [
            [sg.Text('Descrição resumida da tarefa:', font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Multiline('{}'.format(tarefa.descricao), font=fonte_texto)]
        ]

        tarefas = [
            [sg.Text('ID da tarefa: {}'.format(tarefa.id_tarefa), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Nome: {}'.format(tarefa.nome_tarefa), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Data prazo para entrega: {}'.format(tarefa.data_prazo), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Horário prazo para entrega: {}'.format(tarefa.horario_prazo), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [descricao],
            [sg.Text('Matéria correspondente: {}'.format(tarefa.materia_correspondente), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Status da tarefa: {}'.format(tarefa.status_realizado), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Peso: {}'.format(tarefa.peso), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('Nota: {}'.format(tarefa.nota), font=fonte_texto, size=tamanho_texto_mostra_dados)],
            [sg.Text('')]
        ]

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text('Listando tarefas', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [tarefas],
            [sg.Text('')],
            [sg.Cancel('Retornar', font=fonte_texto, size=tamanho_texto)]

        ]

        window = sg.Window('Lista de tarefas', size=(450,580), element_justification="c", grab_anywhere=True).Layout(layout)
        button, values = window.Read()
        window.close()
        return values
    
    def seleciona_tarefa(self, tarefas: list):
        tarefas = [
            [sg.Listbox(values=tarefas, font=fonte_texto, size=(60, 8), key='tarefa')]
        ]

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text('Selecione a Tarefa:', font=fonte_titulo, size=(0,1), text_color=cor_titulo, background_color=fundo_titulo)],
            [tarefas],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Selecionar Tarefa', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button, tarefa = window.Read()
        window.close()
        if button == 'Confirmar':
            id = int((tarefa['tarefa'][0].split())[1])
            return id
        return


    def mostra_mensagem(self, msg):
        layout = [
            [sg.Text(msg, font=fonte_texto, justification='c')],
            [sg.Cancel('Ok', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Aviso!', element_justification="c", grab_anywhere=True).Layout(layout)
        button, msg = window.Read()
        window.close()
        return msg
    
    def mostra_lista(self, tarefas: list):
        tarefas = [
            [sg.Listbox(values=tarefas, font=fonte_texto, size=(60, 8))],
        ]

        layout = [
            [sg.Image(logo2, size=(180, 180))],
            [sg.Text('Listando tarefas', font=('Arial Rounded MT Bold', 10), size=(0, 1), text_color='white')],
            [tarefas],
            [sg.Text('')],
            [sg.Cancel('Retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Lista de tarefas', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button, values = window.Read()
        window.close()
        return values

