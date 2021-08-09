from entidade.Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome: str, email: str, matricula: str):
        super().__init__(nome, email)
        if isinstance(matricula, str):
            self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: str):
        if isinstance(matricula, str):
            self.__matricula = matricula