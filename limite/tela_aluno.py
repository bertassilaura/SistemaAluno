from entidade.aluno import Aluno
from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from limite.temas import *

class TelaAluno(TelaAbstrata):

    def tela_opcoes(self):

        sg.theme(tema)

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text("Você está na página aluno!", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("O que deseja fazer?", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("")],
            [sg.Button("Criar meu cadastro", font=fonte_texto, size=tamanho_texto, key=1)],
            [sg.Button("Mostrar meus dados", font=fonte_texto, size=tamanho_texto, key=2)],
            [sg.Button("Alterar meus dados", font=fonte_texto, size=tamanho_texto, key=3)],
            [sg.Button("Retornar", font=fonte_texto, size=tamanho_texto, key=4)]
        ]
        
        window = sg.Window("Aluno", size=tamanho_janela, element_justification="c", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button, values = window.read()
        window.close()
        return button
        
    def pega_dados(self):

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text("Recebendo seus dados:", font=fonte_titulo, size=(0, 1), text_color=cor_titulo, background_color=fundo_titulo)],
            [sg.Text("")],
            [sg.Text("Nome:", font=fonte_texto, size=tamanho_texto), sg.InputText(key="nome")],
            [sg.Text("Email:", font=fonte_texto, size=tamanho_texto), sg.InputText(key="email")],
            [sg.Text("Matrícula:", font=fonte_texto, size=tamanho_texto), sg.InputText(key="matricula")],
            [sg.Text("")],
            [sg.Submit("Confirmar", font=fonte_texto, size=tamanho_texto), sg.Cancel("Retornar", font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window("Aluno", size=(350,350) , element_justification="c", grab_anywhere=True, default_element_size=(40 , 1)).Layout(layout)
        
        button, dados_aluno = window.read()
        window.close()
        if button == "Confirmar":
            return dados_aluno

    def mostra_dados(self, dados_aluno):

        layout = [
            [sg.Image(logo2, size=(110, 110))],
            [sg.Text('Seus dados:', font=fonte_titulo, size=(0, 1), background_color=fundo_titulo, text_color=cor_titulo)],
            [sg.Text('')],
            [sg.Text(f"Nome: {dados_aluno['nome']}", font=fonte_texto, size=tamanho_texto, justification="c")],
            [sg.Text(f"Email: {dados_aluno['email']}", font=fonte_texto, size=tamanho_texto, justification="c")],
            [sg.Text(f"Matrícula: {dados_aluno['matricula']}", font=fonte_texto, size=tamanho_texto, justification="c")],
            [sg.Text("")],
            [sg.Cancel('Retornar', font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Dados aluno', element_justification="c", size=tamanho_janela, grab_anywhere=True).Layout(layout)
        button, values = window.read()
        window.close()
        return values

    def mostra_mensagem(self, msg):
        sg.theme(tema)
        layout = [
            [sg.Text(msg, font=fonte_texto, size=tamanho_fonte_aviso, justification="c")],
            [sg.Cancel("Ok", font=fonte_texto, size=tamanho_texto)]
        ]

        window = sg.Window('Aviso!', size=tamanho_aviso, element_justification="c", grab_anywhere=True).Layout(layout)
        button, msg = window.read()
        window.close()
        return msg
    
  
