from limite.tela_tarefa import TelaTarefa
from entidade.tarefa import Tarefa

class ControladorTarefa():
  
  def __init__(self, controlador_sistema):
    self.__lista_tarefas = []
    self.__tela_tarefa = TelaTarefa()
    self.__controlador_sistema = controlador_sistema

  #adiciona tarefa
  def adicionar_tarefa(self):
    dados_tarefa = self.__tela_tarefa.pega_dados()

    for tarefa in self.__lista_tarefas:
      if tarefa.nome_tarefa == dados_tarefa["nome_tarefa"]:
        self.__tela_tarefa.mostra_mensagem("Uma tarefa com esse nome já existe!")
        return

    #checa status
    if dados_tarefa["status_realizado"] == "sim":
      dados_tarefa["status_realizado"] = True
    elif dados_tarefa["status_realizado"] == "nao":
      dados_tarefa["status_realizado"] = False

    #checa matéria correspondente
    if dados_tarefa["materia_correspondente"] == "":
        self.__tela_tarefa.mostra_mensagem("Criando Tarefa sem Matéria")
        materia_correspondente = None
    else: 
        materia_correspondente = self.__controlador_sistema.controlador_materia.pega_materia_por_codigo(dados_tarefa["materia_correspondente"].upper())

        if materia_correspondente == None:
          self.__tela_tarefa.mostra_mensagem("Código não existente\nCriando Tarefa sem Matéria, se necessário, altere a Tarefa")
    
    tarefa = Tarefa(dados_tarefa["nome_tarefa"], dados_tarefa["data_prazo"], dados_tarefa["horario_prazo"], dados_tarefa["descricao"], dados_tarefa["status_realizado"], materia_correspondente, dados_tarefa["peso"], dados_tarefa["nota"])
    self.__lista_tarefas.append(tarefa)
    self.__tela_tarefa.mostra_mensagem("Tarefa criada! :)")
    self.listar_tarefas()
  
  #lista todas as tarefas
  def listar_tarefas(self):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("Ainda não existem tarefas !")
      
    else:
      for tarefa in self.__lista_tarefas:

        if tarefa.materia_correspondente == None:
          materia_correspondente = "sem materia"
          self.__tela_tarefa.mostra_dados({"nome_tarefa": tarefa.nome_tarefa, "data_prazo": tarefa.data_prazo, "horario_prazo":tarefa.horario_prazo,
        "descricao": tarefa.descricao, "materia_correspondente": materia_correspondente, "status_realizado": tarefa.status_realizado, "peso": tarefa.peso,
        "nota": tarefa.nota, "id_tarefa": tarefa.id_tarefa})

        else:
          self.__tela_tarefa.mostra_dados({"nome_tarefa": tarefa.nome_tarefa, "data_prazo": tarefa.data_prazo, "horario_prazo":tarefa.horario_prazo,
        "descricao": tarefa.descricao, "materia_correspondente": tarefa.materia_correspondente.nome, "status_realizado": tarefa.status_realizado, "peso": tarefa.peso,
        "nota": tarefa.nota, "id_tarefa": tarefa.id_tarefa})

  #pega tarefa pelo seu nome
  def pega_tarefa_por_id(self, id):
    for tarefa in self.__lista_tarefas:
      if tarefa.id_tarefa == id:
        return tarefa
      return None

  #excluir uma tarefa
  def excluir_tarefa(self):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("Ainda não existem tarefas !")
      return
    
    self.listar_tarefas()
    id = self.__tela_tarefa.seleciona_tarefa()
    tarefa = self.pega_tarefa_por_id(id)

    if(tarefa is not None):
      self.__lista_tarefas.remove(tarefa)
      self.__tela_tarefa.mostra_mensagem("Tarefa removida!")
      self.listar_tarefas()
    else:
      self.__tela_tarefa.mostra_mensagem("ATENÇÃO: Tarefa não existente")
  
  def retornar(self):
    self.__controlador_sistema.abre_tela()

  #lista as tarefas feitas
  def listar_feito(self):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("Ainda não existem tarefas !")
    else:
      for tarefa in self.__lista_tarefas:
        if tarefa.status_realizado == True:
          self.__tela_tarefa.mostra_dados(tarefa) ############### mudar print(tarefa.nome_tarefa)

  #lista as tarefas que ainda devem ser feitas
  def listar_a_fazer(self):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("Ainda não existem tarefas !")
    else:
      for tarefa in self.__lista_tarefas:
        if tarefa.status_realizado == False:
          self.__tela_tarefa.mostra_dados(tarefa) ############### mudar print(tarefa.nome_tarefa)

  def pegar_por_materia(self, materia):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("Ainda não existem tarefas !")
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

  #altera dados da tarefa
  def alterar_tarefa(self):
    if self.__lista_tarefas == []:
      self.__tela_tarefa.mostra_mensagem("Ainda não existem tarefas!")
      return
      
    self.listar_tarefas()
    id = self.__tela_tarefa.seleciona_tarefa()
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
      self.listar_tarefas()
      return

    self.__tela_tarefa.mostra_mensagem("ATENÇÃO: Tarefa não existente")

  def abre_tela(self):
    lista_opcoes = {1: self.adicionar_tarefa, 2: self.excluir_tarefa, 3: self.listar_tarefas, 4: self.listar_feito, 5: self.listar_a_fazer, 6: self.alterar_tarefa, 0: self.retornar}
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_tarefa.tela_opcoes()]()

  

