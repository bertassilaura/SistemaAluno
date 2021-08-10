from limite.tela_tarefa import TelaTarefa
from entidade.tarefa import Tarefa

class ControladorTarefa():
  
  def __init__(self, controlador_sistema):
    lista_tarefas = []
    self.__tela_tarefa = TelaTarefa()
    self.__controlador_sistema = controlador_sistema
