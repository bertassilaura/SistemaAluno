class Professor(Pessoa):

    def __init__(self, telefone: str):
        super().__init__(nome, email)
        self.__telefone = telefone

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone