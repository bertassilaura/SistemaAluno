from entidade.pessoa import Pessoa

class Professor(Pessoa):

    def __init__(self, nome: str, email: str, telefone: str):
        super().__init__(nome, email)
        if isinstance(telefone, str):
            self.__telefone = telefone

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone

    