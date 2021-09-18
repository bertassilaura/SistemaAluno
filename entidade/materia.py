from entidade.professor import Professor

class Materia():

  def __init__(self, nome: str, semestre: str, codigo: str, dia_da_semana: str, horario: str, link: str, classificacao: str, criterio_de_presenca: str, numero_avaliacoes: str, professor: Professor = None):
    self.__nome = nome
    self.__semestre = semestre
    self.__codigo = codigo
    self.__dia_da_semana = dia_da_semana
    self.__horario = horario
    self.__link = link
    self.__classificacao = classificacao
    self.__criterio_de_presenca = criterio_de_presenca
    self.__numero_avaliacoes = numero_avaliacoes
    self.__professor = professor
      
  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome: str):
    if isinstance(nome, str):
      self.__nome = nome

  @property
  def professor(self):
    return self.__professor
  
  @professor.setter
  def professor(self, professor: Professor):
    if isinstance(professor, Professor):
      self.__professor = professor

  @property
  def semestre(self):
    return self.__semestre
  
  @semestre.setter
  def semestre(self, semestre: str):
    if isinstance(semestre, str):
      self.__semestre = semestre

  @property
  def dia_da_semana(self):
    return self.__dia_da_semana
  
  @dia_da_semana.setter
  def dia_da_semana(self, dia_da_semana: str):
    if isinstance(dia_da_semana, str):
      self.__dia_da_semana = dia_da_semana

  @property
  def horario(self):
    return self.__horario

  @horario.setter
  def horario(self, horario: str):
    if isinstance(horario, str):
      self.__horario = horario

  @property
  def link(self):
    return self.__link

  @link.setter
  def link(self, link: str):
    if isinstance(link, str):
      self.__link = link

  @property
  def classificacao(self):
    return self.__classificacao

  @classificacao.setter
  def classificacao(self, classificacao: str):
    if isinstance(classificacao, str):
      self.__classificacao = classificacao

  @property
  def criterio_de_presenca(self):
    return self.__criterio_de_presenca

  @criterio_de_presenca.setter
  def criterio_de_presenca(self, criterio_de_presenca: str):
    if isinstance(criterio_de_presenca, str):
      self.__criterio_de_presenca = criterio_de_presenca

  @property
  def numero_avaliacoes(self):
    return self.__numero_avaliacoes

  @numero_avaliacoes.setter
  def numero_avaliacoes(self, numero_avaliacoes: str):
    if isinstance(numero_avaliacoes, str):
      self.__numero_avaliacoes = numero_avaliacoes

  @property
  def codigo(self):
    return self.__codigo

  @codigo.setter
  def codigo(self, codigo: str):
    if isinstance(codigo, str):
      self.__codigo = codigo