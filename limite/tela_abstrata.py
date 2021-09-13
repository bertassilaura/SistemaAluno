from abc import ABC, abstractmethod

class TelaAbstrata(ABC):

    @abstractmethod
    def abre():
        pass

    @abstractmethod
    def fecha():
        pass
    
    @abstractmethod
    def mostra_mensagem():
        pass



