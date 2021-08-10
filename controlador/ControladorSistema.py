from limite.TelaSistema import TelaSistema
from controlador.ControladorAluno import ControladorAluno
from controlador.ControladorMateria import ControladorMateria
from controlador.ControladorTarefa import ControladorTarefa
from controlador.ControladorProfessor import ControladorProfessor

class ControladorSistema():

    def __init__(self):
        self.__ControladorAluno = ControladorAluno
        self.__ControladorMateria = ControladorMateria
        self.__ControladorTarefa = ControladorTarefa
        self.__ControladorProfessor = ControladorProfessor

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_aluno(self):
        self.__ControladorAluno.abre_tela()

    def cadastra_professor(self):
        self.__ControladorProfessor.abre_tela()

    def cadastra_tarefa(self):
        self.__ControladorTarefa.abre_tela()

    def cadastra_materia(self):
        self.__ControladorMateria.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_aluno, 2: self.cadastra_professor, 3: self.cadastra_tarefa, 4: self.cadastra_materia, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__TelaSistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()


