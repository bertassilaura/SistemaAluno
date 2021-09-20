from limite.tela_tarefa import TelaTarefa
from entidade.tarefa import Tarefa
from persistencia.tarefaDAO import TarefaDAO

class ControladorTarefa():
  
  def __init__(self, controlador_sistema):
    self.__tarefas_dao = TarefaDAO()
    self.__tela_tarefa = TelaTarefa()
    self.__controlador_sistema = controlador_sistema
    self.__id_tarefa = 0

#-----------ADICIONA UMA TAREFA---------------
  def adicionar_tarefa(self):
    list_box_materia = self.__controlador_sistema.controlador_materia.dados_lista_materias()
    dados_tarefa = self.__tela_tarefa.pega_dados(list_box_materia)
    if (dados_tarefa == None) or (self.trata_recebimento_nota(dados_tarefa) == None) or (self.trata_recebimento_peso(dados_tarefa) == None):
      return

    for tarefa in self.__tarefas_dao.get_all():
      if tarefa.nome_tarefa == dados_tarefa["nome_tarefa"]:
        self.__tela_tarefa.mostra_mensagem("Uma tarefa com esse nome já existe!")
        return

    if dados_tarefa["status_realizado"] == "sim":
      dados_tarefa["status_realizado"] = True
    elif dados_tarefa["status_realizado"] == "nao":
      dados_tarefa["status_realizado"] = False

    #checa matéria correspondente
    if dados_tarefa["materia_correspondente"] == "":
        materia_correspondente = None
    else: 
        materia_correspondente = self.__controlador_sistema.controlador_materia.pega_materia_por_id(dados_tarefa["materia_correspondente"]) 
        if materia_correspondente == None:
          self.__tela_tarefa.mostra_mensagem("Código não existente\nCriando Tarefa sem Matéria")
        else:
          materia_correspondente = materia_correspondente
    
    maior = 0
    for tarefa in self.__tarefas_dao.get_all():
      if tarefa.id_tarefa > maior:
        maior = tarefa.id_tarefa
    
    self.__id_tarefa = maior + 1
    
    tarefa = Tarefa(dados_tarefa["nome_tarefa"], dados_tarefa["data_prazo"], dados_tarefa["horario_prazo"], dados_tarefa["descricao"], dados_tarefa["status_realizado"], self.__id_tarefa, materia_correspondente, dados_tarefa["peso"], dados_tarefa["nota"])
    self.__tarefas_dao.add(tarefa)
    self.__tela_tarefa.mostra_mensagem("Tarefa criada! :)")

#-----------TRATA RECEBIMENTO NOTA--------------
  def trata_recebimento_nota(self, dados_tarefa: dict):
    try:
      nota = dados_tarefa['nota']
      nota = float(nota)
      if (type(nota) != float):
        raise ValueError
      return nota
    except ValueError:
      self.__tela_tarefa.mostra_mensagem("Valor de nota inválido: Insira uma valor numérico, inteiro ou decimal !!")
    if (type(nota) == float):
      return nota
#-----------TRATA RECEBIMENTO PESO--------------
  def trata_recebimento_peso(self, dados_tarefa: dict):
    try:
      peso = dados_tarefa['peso']
      peso = float(peso)
      if (type(peso) != float):
        raise ValueError
      return peso
    except ValueError:
      self.__tela_tarefa.mostra_mensagem("Valor de peso inválido: Insira uma valor numérico, inteiro ou decimal !!")
    if (type(peso) == float):
      return peso

#-----------LISTA TODAS AS TAREFAS--------------
  def listar_tarefas(self):
    if self.__tarefas_dao.get_all() == []:
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")

    seleciona = self.__tela_tarefa.seleciona_tarefa(self.dados_lista_tarefas())
    if seleciona != None:
      tarefa = self.pega_tarefa_por_id(seleciona)
      mostra_tarefa = self.__tela_tarefa.mostra_dados(tarefa)

#-----------PEGA TAEFA PELO ID---------------
  def pega_tarefa_por_id(self, id):
    for tarefa in self.__tarefas_dao.get_all():
      if tarefa.id_tarefa == id:
        return tarefa

#-----------RETORNA DADOS ID E NOME DAS TAREFAS---------------
  def dados_lista_tarefas(self):
      return [f'ID: {tarefa.id_tarefa} Nome: {tarefa.nome_tarefa}' for tarefa in self.__tarefas_dao.get_all()] 

#-----------EXCLUI UMA TAREFA---------------
  def excluir_tarefa(self):
    if self.__tarefas_dao.get_all() == []:
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")
      return
    
    id = self.__tela_tarefa.seleciona_tarefa(self.dados_lista_tarefas())
    #tarefa = self.pega_tarefa_por_id(id); antes do dao

    if(id is not None):
      self.__tarefas_dao.remove(id)
      self.__tela_tarefa.mostra_mensagem("Tarefa removida!")


#-----------RETORNA---------------
  def retornar(self):
    self.__controlador_sistema.abre_tela()

#-----------LISTA TAREFAS FEITAS---------------
  def listar_feito(self):
    if self.__tarefas_dao.get_all() == []:
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")
    else:
      lista = []
      for tarefa in self.__tarefas_dao.get_all():
        if tarefa.status_realizado == True:
          lista += [f'ID: {tarefa.id_tarefa} Nome: {tarefa.nome_tarefa}']
      self.__tela_tarefa.mostra_lista(lista)

#-----------LISTA TAREFAS NÃO FEITAS---------------
  def listar_a_fazer(self):
    if self.__tarefas_dao.get_all() == []:
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")
    else:
      lista = []
      for tarefa in self.__tarefas_dao.get_all():
        if tarefa.status_realizado == False:
          lista += [f'ID: {tarefa.id_tarefa} Nome: {tarefa.nome_tarefa}']
      self.__tela_tarefa.mostra_lista(lista)

#-----------PEGA TAREFAS POR MATERIA---------------
  def pegar_por_materia(self, id):
    if self.__tarefas_dao.get_all() == []:
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")
      return

    lista_tarefa_da_materia = []
    vazio = 1
    for tarefa in self.__tarefas_dao.get_all():
      if tarefa.materia_correspondente.id_materia == id:
        vazio = 0
        lista_tarefa_da_materia.append(tarefa) # implementar DAO; lista_tarefa_da_materia.append(tarefa)
    if vazio == 1:
      return None
    else:
      return lista_tarefa_da_materia

#-----------ALTERA UMA TAREFA--------------- 
  def alterar_tarefa(self):
    if self.__tarefas_dao.get_all() == []: # implementar DAO; self.__lista_tarefas
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")
      return

    id = self.__tela_tarefa.seleciona_tarefa(self.dados_lista_tarefas())
    tarefa = self.pega_tarefa_por_id(id)
    list_id_materia = self.__controlador_sistema.controlador_materia.dados_lista_materias()

    if(tarefa is not None):
      novos_dados_tarefa = self.__tela_tarefa.pega_dados(list_id_materia)
      if novos_dados_tarefa != None:
        tarefa.nome_tarefa = novos_dados_tarefa["nome_tarefa"]
        tarefa.data_prazo = novos_dados_tarefa["data_prazo"]
        tarefa.horario_prazo = novos_dados_tarefa["horario_prazo"]
        tarefa.descricao = novos_dados_tarefa["descricao"]
        tarefa.materia_correspondente = self.__controlador_sistema.controlador_materia.pega_materia_por_id(novos_dados_tarefa["materia_correspondente"])
  
        if novos_dados_tarefa["status_realizado"] == "sim":
          tarefa.status_realizado = True
        else:
          tarefa.status_realizado = False

        tarefa.peso = novos_dados_tarefa["peso"]
        tarefa.nota = novos_dados_tarefa["nota"]
        self.__tela_tarefa.mostra_mensagem("Tarefa alterada!")
        self.__tarefas_dao.add(tarefa)
        return
      return

#-----------ABRE TELA---------------
  def abre_tela(self):
    lista_opcoes = {1: self.adicionar_tarefa, 2: self.excluir_tarefa, 3: self.listar_tarefas, 4: self.listar_feito, 5: self.listar_a_fazer, 6: self.alterar_tarefa, 7: self.retornar}
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_tarefa.tela_opcoes()]()