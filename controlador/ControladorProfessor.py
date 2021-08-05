from controlador.ControladorSistema import ControladorSistema
from limite.TelaProfessor import TelaProfessor
from entidade.Professor import Professor

class ControladorProfessor():

    def __init__(self, Controlador_Sistema):
        self.__lista_professores = []
        self.__TelaProfessor = TelaProfessor()
        self.__ControladorSistema = ControladorSistema

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_professor, 2: self.excluir_professor, 3: self.lista_professor, 4: self.retornar()}
