from persistencia.DAO import DAO
from entidade.tarefa import Tarefa

class TarefaDAO(DAO):

    def __init__(self):
        super().__init__('tarefa.pkl')
    
    def add(self, tarefa: Tarefa):
        if (tarefa is not None) and isinstance(tarefa, Tarefa):
            super().add(tarefa.id_tarefa, tarefa)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)
    