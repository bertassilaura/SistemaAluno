from limite.tela_tarefa import TelaTarefa
from entidade.tarefa import Tarefa

class ControladorTarefa():
  
  def __init__(self, controlador_sistema):
    self.__lista_tarefas = []
    self.__tela_tarefa = TelaTarefa()
    self.__controlador_sistema = controlador_sistema

#-----------ADICIONA UMA TAREFA---------------
  def adicionar_tarefa(self):
    dados_tarefa = self.__tela_tarefa.pega_dados()
    if (dados_tarefa == None) or (self.trata_recebimento_nota(dados_tarefa) == None):
      return

    else:

      for tarefa in self.__lista_tarefas:
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
          materia_correspondente = self.__controlador_sistema.controlador_materia.pega_materia_por_codigo(dados_tarefa["materia_correspondente"].upper())

          if materia_correspondente == None:
            self.__tela_tarefa.mostra_mensagem("Código não existente\nCriando Tarefa sem Matéria, se necessário, altere a Tarefa")
      
      tarefa = Tarefa(dados_tarefa["nome_tarefa"], dados_tarefa["data_prazo"], dados_tarefa["horario_prazo"], dados_tarefa["descricao"], dados_tarefa["status_realizado"], materia_correspondente, dados_tarefa["peso"], dados_tarefa["nota"])
      self.__lista_tarefas.append(tarefa)
      self.__tela_tarefa.mostra_mensagem("Tarefa criada! :)")

#-----------TRATA RECEBIMENTO NOTA--------------
  def trata_recebimento_nota(self, dados_tarefa: dict):
    try:
      nota = dados_tarefa['nota']
      nota = float(nota)
      if type(nota) != float:
        raise ValueError
      return nota
    except ValueError:
      self.__tela_tarefa.mostra_mensagem("Valor de nota inválido: Insira uma valor numérico, inteiro ou decimal !!")
    if type(nota) == float:
      return nota

#-----------LISTA TODAS AS TAREFAS--------------
  def listar_tarefas(self):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")
    else:
      seleciona = self.__tela_tarefa.seleciona_tarefa(self.dados_lista_tarefas())
      if seleciona != None:
        tarefa = self.pega_tarefa_por_id(seleciona)
        mostra_tarefa = self.__tela_tarefa.mostra_dados(tarefa)
        return mostra_tarefa
      return

#-----------PEGA TAEFA PELO ID---------------
  def pega_tarefa_por_id(self, id):
    for tarefa in self.__lista_tarefas:
      if tarefa.id_tarefa == id:
        return tarefa
      return None

#-----------RETORNA DADOS ID E NOME DAS TAREFAS---------------
  def dados_lista_tarefas(self):
      return [f'ID: {tarefa.id_tarefa} Nome: {tarefa.nome_tarefa}' for tarefa in self.__lista_tarefas]

#-----------EXCLUI UMA TAREFA---------------
  def excluir_tarefa(self):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")
      return
    
    id = self.__tela_tarefa.seleciona_tarefa(self.dados_lista_tarefas())
    tarefa = self.pega_tarefa_por_id(id)

    if(tarefa is not None):
      self.__lista_tarefas.remove(tarefa)
      self.__tela_tarefa.mostra_mensagem("Tarefa removida!")

#-----------RETORNA---------------
  def retornar(self):
    self.__controlador_sistema.abre_tela()

#-----------LISTA TAREFAS FEITAS---------------
  def listar_feito(self):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")
    else:
      lista = []
      for tarefa in self.__lista_tarefas:
        if tarefa.status_realizado == True:
          lista += [[f'ID: {tarefa.id_tarefa} Nome: {tarefa.nome_tarefa}']]
      self.__tela_tarefa.mostra_lista(lista) #printando como dicionario

#-----------LISTA TAREFAS NÃO FEITAS---------------
  def listar_a_fazer(self):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")
    else:
      lista = []
      for tarefa in self.__lista_tarefas:
        if tarefa.status_realizado == False:
          lista += [[f'ID: {tarefa.id_tarefa} Nome: {tarefa.nome_tarefa}']]
      self.__tela_tarefa.mostra_lista(lista) #printando como dicionario

#-----------PEGA TAREFAS POR MATERIA---------------
  def pegar_por_materia(self, materia):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")
      return

    lista_tarefa_da_materia = []
    vazio = 1
    for tarefa in self.__lista_tarefas:
      if tarefa.materia_correspondente.codigo == materia:
        vazio = 0
        lista_tarefa_da_materia.append(tarefa)
    if vazio == 1:
      return None
    else:
      return lista_tarefa_da_materia

#-----------ALTERA UMA TAREFA--------------- 
  def alterar_tarefa(self):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("A lista de tarefas está vazia !")
      return

    id = self.__tela_tarefa.seleciona_tarefa(self.dados_lista_tarefas())
    tarefa = self.pega_tarefa_por_id(id)

    if(tarefa is not None):
      novos_dados_tarefa = self.__tela_tarefa.pega_dados()
      tarefa.nome_tarefa = novos_dados_tarefa["nome_tarefa"]
      tarefa.data_prazo = novos_dados_tarefa["data_prazo"]
      tarefa.horario_prazo = novos_dados_tarefa["horario_prazo"]
      tarefa.descricao = novos_dados_tarefa["descricao"]
      tarefa.materia_correspondente = novos_dados_tarefa["materia_correspondente"]

      if novos_dados_tarefa["status_realizado"] == "sim":
        tarefa.status_realizado = True
      else:
        tarefa.status_realizado = False

      tarefa.peso = novos_dados_tarefa["peso"]
      tarefa.nota = novos_dados_tarefa["nota"]
      self.__tela_tarefa.mostra_mensagem("Tarefa alterada!")
      return

#-----------ABRE TELA---------------
  def abre_tela(self):
    lista_opcoes = {1: self.adicionar_tarefa, 2: self.excluir_tarefa, 3: self.listar_tarefas, 4: self.listar_feito, 5: self.listar_a_fazer, 6: self.alterar_tarefa, 0: self.retornar}
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_tarefa.tela_opcoes()]()

  

