from entidade.pessoa import Pessoa

class Professor(Pessoa):

    id = 0

    def __init__(self, nome: str, email: str, telefone: str):
        super().__init__(nome, email)
        if isinstance(telefone, str):
            self.__telefone = telefone
        self.__id_professor = Professor.id
        Professor.id += 1

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone

    @property
    def id_professor(self):
        return self.__id_professor

    