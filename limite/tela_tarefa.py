from entidade.tarefa import Tarefa
from PySimpleGUI.PySimpleGUI import InputText
from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaTarefa(TelaAbstrata):

    def le_numero_inteiro():
        pass
    
    def tela_opcoes(self):

        layout  = [
            [sg.Text('Tarefa')],
            [sg.Button('Adicionar Tarefa', key=1)],
            [sg.Button('Excluir Tarefa', key=2)],
            [sg.Button('Listar Tarefas', key=3)],
            [sg.Button('Listar tarefas feitas', key=4)],
            [sg.Button('Listar tarefas a fazer', key=5)],
            [sg.Button('Alterar Tarefa', key=6)],
            [sg.Exit('Retornar', key=0)]
        ]

        window = sg.Window('Tela Tarefa').Layout(layout)
        button, values = window.Read()
        window.close()
        return button

    def pega_dados(self):

        layout = [
            [sg.Text('Insira os dados')],
            [sg.Text('Nome'), sg.InputText('', key = 'nome_tarefa')],
            [sg.Text('Data prazo para entrega'), sg.InputText('', key = 'data_prazo')], 
            [sg.Text('Horário prazo para entrega'), sg.InputText('', key = 'horario_prazo')], #sg.Spin([i for i in range(0,23)]), sg.Spin([i for i in range(0,59)])
            [sg.Text('Descrição resumida da tarefa'), sg.Multiline(default_text= 'Descrição resumida da tarefa', key = 'descricao')],
            [sg.Text('Está feita ou não?'), sg.InputCombo(('sim', 'não'),key = 'status_realizado')],
            [sg.Text('Digite o código da matéria correspondente. Se ainda não criou a materia, ou essa tarefa nao possui materia, deixe em branco'), sg.InputText('',  key = 'materia_correspondente')],
            [sg.Text('Peso'), sg.Spin([i for i in range(0,101)], initial_value='selecione', key = 'peso')], # receber float
            [sg.Text('Nota'), sg.InputText('', key = 'nota')], # Colocar layout para notas, receber float
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar e retornar')]
        ]

        window = sg.Window('Dados da tarefa').Layout(layout)
        button, dados_tarefa = window.Read()
        window.close()
        if button == 'Confirmar':
            return dados_tarefa

    def mostra_dados(self, tarefa: Tarefa):

        tarefas = [
            [sg.Text('ID da tarefa: {}'.format(tarefa.id_tarefa))],
            [sg.Text('Nome: {}'.format(tarefa.nome_tarefa))],
            [sg.Text('Data prazo para entrega: {}'.format(tarefa.data_prazo))],
            [sg.Text('Horário prazo para entrega: {}'.format(tarefa.horario_prazo))],
            [sg.Text('Descrição resumida da tarefa: {}'.format(tarefa.descricao))],
            [sg.Text('matéria correspondente: {}'.format(tarefa.materia_correspondente))],
            [sg.Text('Status da tarefa: {}'.format(tarefa.status_realizado))],
            [sg.Text('Peso: {}'.format(tarefa.peso))],
            [sg.Text('Nota: {}'.format(tarefa.nota))],
            [sg.Text('')]
        ]

        layout = [
            [sg.Text('Listando tarefas')],
            [tarefas],
            [sg.Text('')],
            [sg.Cancel('Retornar')]

        ]

        window = sg.Window('Lista de tarefas').Layout(layout)
        button, values = window.Read()
        window.close()
        return values

    def seleciona_tarefa(self):
        layout = [
            [sg.Text('ID da tarefa que deseja selecionar'), sg.InputText('', key='id')],
            [sg.Submit('Confirmar'), sg.Cancel('Retornar')]
        ]

        window = sg.Window('Selecionar Tarefa').Layout(layout)
        button, id = window.Read()
        id = int(id['id']) # transformar e tratar no controlador
        window.close()
        return id   


    def mostra_mensagem(self, msg):

        layout = [
            [sg.Text(msg)],
            [sg.Cancel('Ok')]
        ]

        window = sg.Window('Aviso!').Layout(layout)
        button, msg = window.Read()
        window.close()
        return msg

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


'''def seleciona_tarefa(self, tarefa: Tarefa):

        tarefa = [
            [sg.Text('ID da tarefa: {}'.format(tarefa.id_tarefa))],
            [sg.Text('Nome: {}'.format(tarefa.nome_tarefa))],
        ]

        layout = [
            [sg.Button(tarefa, key='id')],
            [sg.Submit('Confirmar'), sg.Cancel('Retornar')],
        ]

        window = sg.Window('Selecionar Tarefa').Layout(layout)
        button, id = window.Read()
        id = int(id['id']) # transformar e tratar no controlador
        window.close()
        return id'''