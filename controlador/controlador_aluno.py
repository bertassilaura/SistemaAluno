from limite.tela_aluno import TelaAluno
from entidade.aluno import Aluno

class ControladorAluno():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_aluno = TelaAluno()
        self.__aluno = None
    
    # Fazer tratamento de dados 
    def criar_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados()
        self.__aluno = Aluno(dados_aluno["nome"], dados_aluno["email"], dados_aluno["matricula"])    

    def mostra_aluno(self):
        return self.__tela_aluno.mostra_dados({"nome": self.__aluno.nome, "email": self.__aluno.email, "matricula": self.__aluno.matricula})
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_aluno, 2: self.mostra_aluno, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
