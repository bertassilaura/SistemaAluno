from limite.tela_sistema import TelaSistema
from controlador.controlador_aluno import ControladorAluno
from controlador.controlador_materia import ContorladorMateria
from controlador.controlador_tarefa import ControladorTarefa
from controlador.controlador_professor import ControladorProfessor

class ControladorSistema():

    def __init__(self):
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_materia = ContorladorMateria(self)
        self.__controlador_tarefa = ControladorTarefa(self)
        self.__controlador_professor = ControladorProfessor(self) 
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_aluno(self):
        self.__controlador_aluno.abre_tela()

    def cadastra_professor(self):
        self.__controlador_professor.abre_tela()

    def cadastra_tarefa(self):
        self.__controlador_tarefa.abre_tela()

    def cadastra_materia(self):
        self.__controlador_materia.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_aluno, 2: self.cadastra_professor, 3: self.cadastra_tarefa, 4: self.cadastra_materia, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    


