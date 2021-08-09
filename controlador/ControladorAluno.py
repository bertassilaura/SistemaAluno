from limite.TelaAluno import TelaAluno
from entidade.Aluno import Aluno
from controlador.ControladorSistema import ControladorSistema

class ControladorAluno():
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_aluno = TelaAluno()
        self.__aluno = None
    
    # Fazer tratamento de dados 
    def criar_aluno(self, nome: str, email: str, matricula: str):
        while True:
            try:
                if nome == int(nome) or email == int(email) or not(matricula == int(matricula)):
                    raise ValueError
            except ValueError:
                print("Valor incorreto: ""criar_aluno"" só aceita valores do tipo ""str"" como parâmetro !")
            else:
                self.__aluno = Aluno(nome, email, matricula)
    
    
    def mostra_aluno(self):
        return self.__tela_aluno.mostra_dados({"nome": self.__aluno.nome, "email": self.__aluno.email, "matricula": self.__aluno.matricula})
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_aluno, 2: self.mostra_aluno, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
