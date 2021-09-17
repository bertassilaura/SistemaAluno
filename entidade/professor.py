from entidade.pessoa import Pessoa

class Professor(Pessoa):

    def __init__(self, nome: str, email: str, telefone: str, id_professor: int):
        super().__init__(nome, email)
        if isinstance(telefone, str):
            self.__telefone = telefone
        self.__id_professor = id_professor
        

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

    