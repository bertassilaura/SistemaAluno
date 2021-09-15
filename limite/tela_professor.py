from PySimpleGUI.PySimpleGUI import Window
from entidade.professor import Professor
from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from limite.temas import *

class TelaProfessor(TelaAbstrata):

    sg.theme(tema)

    def tela_opcoes(self):

        sg.theme(tema)

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text("Você está na página professor!", font=fonte_titulo, size=(0, 1), background_color=fundo_titulo, text_color=cor_titulo)],
            [sg.Text("O que deseja fazer?", font=fonte_titulo, size=(0, 1), background_color=fundo_titulo, text_color=cor_titulo)],
            [sg.Text("")],
            [sg.Button("Adicionar Professor", font=fonte_texto, size=tamanho_texto, key=1)],
            [sg.Button("Excluir Professor", font=fonte_texto, size=tamanho_texto, key=2)],
            [sg.Button("Listar professores", font=fonte_texto, size=tamanho_texto, key=3)],
            [sg.Button("Alterar Professor", font=fonte_texto, size=tamanho_texto, key=4)],
            [sg.Button("Retornar", font=fonte_texto, size=tamanho_texto, key=0)]
        ]
        
        window = sg.Window("Professor", size=tamanho_janela, element_justification="c", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button, values = window.Read()
        window.close()
        return button
        
    def pega_dados(self):
        
        sg.theme(tema)

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text("Pegando dados do professor:", font=fonte_titulo, size=(0, 1), background_color=fundo_titulo, text_color=cor_titulo)],
            [sg.Text("")],
            [sg.Text("Nome:", font=fonte_texto, size=tamanho_texto), sg.InputText(key="nome")],
            [sg.Text("Email:", font=fonte_texto, size=tamanho_texto), sg.InputText(key="email")],
            [sg.Text("Telefone:", font=fonte_texto, size=tamanho_texto), sg.InputText(key="telefone")],
            [sg.Text("")],
            [sg.Submit("Confirmar", font=fonte_texto, size=tamanho_texto), sg.Cancel("Retornar")]
        ]

        window = sg.Window("Professor", size=tamanho_janela, element_justification="c", default_element_size=(40 , 1)).Layout(layout)
        
        button, dados_professor = window.read()
        window.close()
        if button == "Confirmar":
            return dados_professor
    
    def mostra_dados(self, professor: Professor):
        
        professores = [
            [sg.Text("Dados do professor:", font=fonte_titulo, size=(0, 1), background_color=fundo_titulo, text_color=cor_titulo)],
            [sg.Text("")],
            [sg.Text(f"ID: {professor.id_professor}", font=fonte_texto, size=tamanho_texto)],
            [sg.Text(f"Nome: {professor.nome}", font=fonte_texto, size=tamanho_texto)],
            [sg.Text(f"Email: {professor.email}", font=fonte_texto, size=tamanho_texto)],
            [sg.Text(f"Telefone: {professor.telefone}", font=fonte_texto, size=tamanho_texto)],
            [sg.Text("")],
        ]

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [professores],
            [sg.Text("")],
            [sg.Cancel("Retornar", font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window("Professor", size=tamanho_janela, element_justification="c", default_element_size=(40 , 1)).Layout(layout)
        
        button, values = window.read()
        window.close()
        if button == "Confirmar":
            return values

    def mostra_mensagem(self, msg):
        sg.theme(tema)
        layout = [
            [sg.Text(msg, font=fonte_texto, size=tamanho_fonte_aviso)],
            [sg.Cancel("Ok", font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Aviso!', size=tamanho_aviso, element_justification="c", grab_anywhere=True).Layout(layout)
        button, msg = window.Read()
        window.close()
        return msg

    def seleciona_professor(self, professores):

        professores = [
            [sg.Listbox(values=professores, font=fonte_texto, size=tamanho_texto, key="professor")]
        ]
        
        layout = [
            [sg.Image(logo2, size=(180, 180))],
            [sg.Text("Selecione o professor:", font=fonte_titulo, size=(0, 1), background_color=fundo_titulo, text_color=cor_titulo)],
            [sg.Text("")],
            [professores],
            [sg.Text("")],
            [sg.Submit("Confirmar", font=fonte_texto, size=tamanho_texto), sg.Cancel("Retornar", font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Selecionar Professor', size=tamanho_janela, element_justification="c", grab_anywhere=True).Layout(layout)
        button, professor = window.read()
        window.close()
        if button == 'Confirmar':
            id = int((professor['professor'][0].split())[1])
            return id
        return