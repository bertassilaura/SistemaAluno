from entidade.Pessoa import Pessoa

class Professor(Pessoa):

    def __init__(self, telefone: str):
        super().__init__()
        self.__telefone = telefone

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone

    