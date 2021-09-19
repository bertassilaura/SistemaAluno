from persistencia.DAO import DAO
from entidade.materia import Materia

class MateriaDAO(DAO):

  def __init__(self):
    super().__init__('data/materia.pkl')
  
  def add(self, materia: Materia):
    if (materia is not None) and isinstance(materia, Materia):
      super().add(materia.id_materia, materia)
  
  def remove(self, key: int):
    if isinstance(key, int):
      return super().remove(key)

  def get(self, key: int):
    if isinstance(key, int):
      return super().get(key)