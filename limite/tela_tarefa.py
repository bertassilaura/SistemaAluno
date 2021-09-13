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
            [sg.Image(logo, size=(180, 180))],
            [sg.Text('Tarefa', font=("Arial Rounded MT Bold", 30), size=tamanho_texto, justification='c', text_color= 'white')],
            [sg.Button('Adicionar Tarefa', font=fonte_texto, size=tamanho_texto, key=1)],
            [sg.Button('Excluir Tarefa', font=fonte_texto, size=tamanho_texto, key=2)],
            [sg.Button('Listar Tarefas', font=fonte_texto, size=tamanho_texto, key=3)],
            [sg.Button('Listar tarefas feitas', font=fonte_texto, size=tamanho_texto, key=4)],
            [sg.Button('Listar tarefas a fazer', font=fonte_texto, size=tamanho_texto, key=5)],
            [sg.Button('Alterar Tarefa', font=fonte_texto, size=tamanho_texto, key=6)],
            [sg.Exit('Retornar', font=fonte_texto, size=tamanho_texto, key=0)]
        ]

        window = sg.Window('Tela Tarefa', size=(tamanho_janela), element_justification="c", grab_anywhere=True, default_element_size=(40, 1)).Layout(layout)
        button, values = window.Read()
        window.close()
        return button

    def pega_dados(self):

        layout = [
            [sg.Text('Insira os dados', font=fonte_texto, size=tamanho_texto)],
            [sg.Text('Nome', font=fonte_texto, size=tamanho_texto), sg.InputText('Atribua um nome para a tarefa', key = 'nome_tarefa')],
            [sg.Text('Data prazo para entrega', font=fonte_texto, size=tamanho_texto), sg.InputText('DD/MM/AA', key = 'data_prazo')], 
            [sg.Text('Horário prazo para entrega', font=fonte_texto, size=tamanho_texto), sg.InputText('00:00', key = 'horario_prazo')], #sg.Spin([i for i in range(0,23)]), sg.Spin([i for i in range(0,59)])
            [sg.Text('Descrição', font=fonte_texto, size=tamanho_texto), sg.Multiline(default_text= 'Descrição resumida da tarefa', key = 'descricao')],
            [sg.Text('Está feita ou não?', font=fonte_texto, size=tamanho_texto), sg.InputCombo(('sim', 'não'),default_value='selecione',key = 'status_realizado')],
            [sg.Text('Código-Matéria correspondente', font=fonte_texto, size=tamanho_texto), sg.InputText('Se não criou a materia, ou nao possui materia, deixe em branco',  key = 'materia_correspondente')],
            [sg.Text('Peso', font=fonte_texto, size=tamanho_texto), sg.Spin([i for i in range(0,101)], initial_value='selecione', key = 'peso')], # receber float
            [sg.Text('Nota', font=fonte_texto, size=tamanho_texto), sg.InputText('Exemplo: 8.5', key = 'nota')], # Colocar layout para notas, receber float
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Cancelar e retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Dados da tarefa', grab_anywhere=True).Layout(layout)
        button, dados_tarefa = window.Read()
        window.close()
        if button == 'Confirmar':
            return dados_tarefa

    def mostra_dados(self, tarefa: Tarefa):
        tarefas = [
            [sg.Text('ID da tarefa: {}'.format(tarefa.id_tarefa), font=fonte_texto, size=tamanho_texto)],
            [sg.Text('Nome: {}'.format(tarefa.nome_tarefa), font=fonte_texto, size=tamanho_texto)],
            [sg.Text('Data prazo para entrega: {}'.format(tarefa.data_prazo), font=fonte_texto, size=tamanho_texto)],
            [sg.Text('Horário prazo para entrega: {}'.format(tarefa.horario_prazo), font=fonte_texto, size=tamanho_texto)],
            [sg.Text('Descrição resumida da tarefa: {}'.format(tarefa.descricao), font=fonte_texto, size=tamanho_texto)],
            [sg.Text('Matéria correspondente: {}'.format(tarefa.materia_correspondente), font=fonte_texto, size=tamanho_texto)],
            [sg.Text('Status da tarefa: {}'.format(tarefa.status_realizado), font=fonte_texto, size=tamanho_texto)],
            [sg.Text('Peso: {}'.format(tarefa.peso), font=fonte_texto, size=tamanho_texto)],
            [sg.Text('Nota: {}'.format(tarefa.nota), font=fonte_texto, size=tamanho_texto)],
            [sg.Text('')]
        ]

        layout = [
            [sg.Image(logo2, size=(180, 180))],
            [sg.Text('Listando tarefas', font=fonte_texto, size=tamanho_texto)],
            [tarefas],
            [sg.Text('')],
            [sg.Cancel('Retornar', font=fonte_texto, size=tamanho_texto)]

        ]

        window = sg.Window('Lista de tarefas', grab_anywhere=True).Layout(layout)
        button, values = window.Read()
        window.close()
        return values
    
    def seleciona_tarefa(self, tarefas: list):
        tarefas = [
            [sg.Listbox(values=tarefas, font=fonte_texto, size=(30, 6), key='tarefa')]
        ]

        layout = [
            [sg.Image(logo2, size=(180, 180))],
            [sg.Text('Selecione a Tarefa:', font=fonte_texto, size=(0, 2))],
            [tarefas],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto, size=tamanho_texto), sg.Cancel('Retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Selecionar Tarefa', grab_anywhere=True).Layout(layout)
        button, tarefa = window.Read()
        window.close()
        if button == 'Confirmar':
            id = int((tarefa['tarefa'][0].split())[1])
            return id
        return


    def mostra_mensagem(self, msg):
        layout = [
            [sg.Text(msg, font=fonte_texto, size=(30,6))],
            [sg.Cancel('Ok', font=fonte_texto, size=(30,6))]
        ]

        window = sg.Window('Aviso!', grab_anywhere=True).Layout(layout)
        button, msg = window.Read()
        window.close()
        return msg
    
    def mostra_lista(self, tarefas: list):
        tarefas = [
            [sg.Listbox(values=tarefas, font=fonte_texto, size=(30, 6))],
        ]

        layout = [
            [sg.Image(logo2, size=(180, 180))],
            [sg.Text('Listando tarefas', font=fonte_texto, size=tamanho_texto)],
            [tarefas],
            [sg.Text('')],
            [sg.Cancel('Retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Lista de tarefas', grab_anywhere=True).Layout(layout)
        button, values = window.Read()
        window.close()
        return values


'''# Passar tratamento de dados do pega dados para o controlador
        while True:
            try:
                peso = float(peso)
                if type(peso) != float:
                    raise ValueError
            except ValueError:
                self.mostra_mensagem("Valor de peso inválido: Insira uma valor numérico, inteiro ou decimal !!")
            if type(peso) == float:
                break

        # Passar tratamento de dados do pega dados para o controlador    
        while True:
            try:
                nota = float(nota)
                if type(nota) != float:
                    raise ValueError
            except ValueError:
                self.mostra_mensagem("Valor de nota inválido: Insira uma valor numérico, inteiro ou decimal !!")
            if type(nota) == float:
                break'''


'''def seleciona_tarefa(self):
        layout = [
            [sg.Text('ID da tarefa que deseja selecionar'), sg.InputText('', key='id')],
            [sg.Submit('Confirmar'), sg.Cancel('Retornar')]
        ]

        window = sg.Window('Selecionar Tarefa').Layout(layout)
        button, id = window.Read()
        id = int(id['id']) # transformar e tratar no controlador
        window.close()
        return id'''