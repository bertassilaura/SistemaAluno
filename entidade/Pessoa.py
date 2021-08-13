class Pessoa():

    def __init__(self, nome: str, email: str):
        
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(email, str):
            self.__email = email

    @property
    def nome(self):
        return self.__nome 

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        if isinstance(email, str):
            self.__email = email