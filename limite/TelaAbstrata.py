from ABC import ABC, abstractmethod

class TelaAbstrata():

    @abstractmethod
    def tela_opcoes():
        pass

    @abstractmethod
    def le_num_inteiro():
        pass

    @abstractmethod
    def pega_dados():
        pass

    @abstractmethod
    def mostra_dados():
        pass
