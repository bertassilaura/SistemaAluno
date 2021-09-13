from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from limite.temas import *

class TelaProfessor(TelaAbstrata):

    sg.theme(tema)

    def tela_opcoes(self):

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text("Você está na página professor!", font=fonte_titulo, size=(0, 1))],
            [sg.Text("O que deseja fazer?", font=fonte_titulo, size=(0, 1))],
            [sg.Text("")],
            [sg.Button("Adicionar Professor", font=fonte_texto, size=tamanho_texto)],
            [sg.Button("Excluir Professor", font=fonte_texto, size=tamanho_texto)],
            [sg.Button("Listar professores", font=fonte_texto, size=tamanho_texto)],
            [sg.Button("Alterar Professor", font=fonte_texto, size=tamanho_texto)],
            [sg.Button("Retornar", font=fonte_texto, size=tamanho_texto)]
        ]
        
        window = sg.Window("Aluno", size=tamanho_janela, element_justification="c", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button = window.read()
        valor_selecionado = {"Adicionar Professor": 1, "Excluir Professor": 2, "Listar professores": 3, "Alterar Professor": 4, "Retornar": 0}
        window.close()
        return valor_selecionado[button[0]]
        
    def pega_dados(self):

        layout = [
            [sg.Text("Adicionar Professor:")],
            [sg.Text("Nome:"), sg.InputText()],
            [sg.Text("Email:"), sg.InputText()],
            [sg.Text("Telefone:"), sg.InputText()],
            [sg.Submit("Confirmar"), sg.Cancel("Retornar")]
        ]

        window = sg.Window("Aluno", default_element_size=(40 , 1)).Layout(layout)
        
        valores = window.read()
        valor_selecionado = valores[0]
        input_user = valores[1][0].strip()

        window.close()
        if valor_selecionado == "Confirmar" and input_user != "":
            return input_user

    def mostra_mensagem(self, msg):
        print(msg)

    def abre(self):
        pass

    def fecha(self):
        pass
