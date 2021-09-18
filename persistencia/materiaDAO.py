from persistencia.DAO import DAO
from entidade.materia import Materia

class MateriaDAO(DAO):

  def __init__(self):
    super().__init__('data/materia.pkl')
  
  def add(self, materia: Materia):
    if (materia is not None) and isinstance(materia, Materia):
      super().add(materia.codigo, materia)
  
  def remove(self, key: str):
    if isinstance(key, str):
      return super().remove(key)

  def get(self, key: str):
    if isinstance(key, str):
      return super().get(key)