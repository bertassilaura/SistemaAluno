from abc import ABC, abstractmethod

class TelaAbstrata(ABC):
    
    @abstractmethod
    def mostra_mensagem():
        pass

    @abstractmethod
    def tela_opcoes():
        pass

    @abstractmethod
    def pega_dados():
        pass

    @abstractmethod
    def mostra_dados():
        pass


