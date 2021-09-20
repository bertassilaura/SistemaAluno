from entidade.materia import Materia 

class Tarefa:

  def __init__(self, nome_tarefa: str, data_prazo: str , horario_prazo: str, descricao: str, status_realizado: bool, id_tarefa: int, materia_correspondente: Materia = None, peso: float = 0, nota: float = 0):
    self.__nome_tarefa = nome_tarefa
    self.__data_prazo = data_prazo
    self.__horario_prazo = horario_prazo
    self.__descricao = descricao
    self.__materia_correspondente = materia_correspondente
    self.__status_realizado = status_realizado
    self.__peso = peso
    self.__nota = nota
    self.__id_tarefa = id_tarefa         
          
  @property
  def nome_tarefa(self):
    return self.__nome_tarefa
  
  @nome_tarefa.setter
  def nome_tarefa(self, nome_tarefa: str):
    if isinstance(nome_tarefa, str):
        self.__nome_tarefa = nome_tarefa
  
  @property
  def data_prazo(self):
      return self.__data_prazo
  
  @data_prazo.setter
  def data_prazo(self, data_prazo: str):
      if isinstance(data_prazo, str):
          self.__data_prazo = data_prazo
  
  @property
  def horario_prazo(self):
      return self.__horario_prazo

  @horario_prazo.setter
  def horario_prazo(self, horario_prazo: str):
      if isinstance(horario_prazo, str):
          self.__horario_prazo = horario_prazo
  
  @property
  def descricao(self):
      return self.__descricao
  
  @descricao.setter
  def descricao(self, descricao: str):
      if isinstance(descricao, str):
          self.__descricao = descricao
  
  @property
  def nota(self):
      return self.__nota
  
  @nota.setter
  def nota(self, nota: float):
        self.__nota = nota
  
  @property
  def materia_correspondente(self):
      return self.__materia_correspondente

  @materia_correspondente.setter
  def materia_correspondente(self, materia_correspondente: Materia):
      if isinstance(materia_correspondente, Materia):
          self.__materia_correspondente = materia_correspondente
  
  @property
  def status_realizado(self):
      return self.__status_realizado
  
  @status_realizado.setter
  def status_realizado(self, status_realizado: bool):
      if isinstance(status_realizado, bool):
          self.__status_realizado = status_realizado

  @property
  def peso(self):
      return self.__peso
  
  @peso.setter
  def peso(self, peso: float):
      self.__peso = peso

  @property
  def id_tarefa(self):
      return self.__id_tarefa
    