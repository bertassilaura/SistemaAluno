from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from limite.temas import *

class TelaSistema(TelaAbstrata):

    def tela_opcoes(self):

        sg.theme(tema)

        layout = [
            [sg.Image(logo, size=(180, 180))],
            [sg.Text("Escolha uma opção: ", font=fonte_titulo, size=(0,1))],
            [sg.Text("")],
            [sg.Button("Aluno", font=fonte_texto, size=tamanho_texto)],
            [sg.Button("Professores", font=fonte_texto, size=tamanho_texto)],
            [sg.Button("Matéria", font=fonte_texto, size=tamanho_texto)],
            [sg.Button("Tarefa", font=fonte_texto, size=tamanho_texto)],
            [sg.Button("Encerrar Sistema", font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window("Início", size=(tamanho_janela), element_justification="c", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button = window.read()
        valor_selecionado = {"Aluno": 1, "Professores": 2, "Matéria": 3, "Tarefa": 4, "Encerrar Sistema": 0}
        window.close()
        return valor_selecionado[button[0]]


    def abre(self):
        pass
    
    def fecha(self):
        pass

    def mostra_mensagem(self):
        pass

