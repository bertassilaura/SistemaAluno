from limite.tela_tarefa import TelaTarefa
from entidade.tarefa import Tarefa

class ControladorTarefa():
  
  def __init__(self, controlador_sistema):
    self.__lista_tarefas = []
    self.__tela_tarefa = TelaTarefa()
    self.__controlador_sistema = controlador_sistema

  def adicionar_tarefa(self):
    dados_tarefa = self.__tela_tarefa.pega_dados()

    #checa status
    if dados_tarefa["status_realizado"] == "sim":
      dados_tarefa["status_realizado"] = True
    elif dados_tarefa["status_realizado"] == "nao":
      dados_tarefa["status_realizado"] = False

    #checa matéria correspondente
    if dados_tarefa["materia_correspondente"] == "":
        print("Criando Tarefa sem Matéria.")
        materia_correspondente = None
    else: 
        materia_correspondente = self.__controlador_sistema.controlador_materia.pega_materia_por_codigo(dados_tarefa["materia_correspondente"])

        if materia_correspondente == None:
          print("Código não existente. Criando Tarefa sem Matéria, se necessário, altere a Tarefa")
    
    #cria tarefa
    tarefa = Tarefa(dados_tarefa["nome_tarefa"], dados_tarefa["data_prazo"], dados_tarefa["horario_prazo"], dados_tarefa["descricao"], dados_tarefa["status_realizado"], materia_correspondente, dados_tarefa["peso"], dados_tarefa["nota"])
    self.__lista_tarefas.append(tarefa)
    print(f"Tarefa criada! :)")
  
  #lista todas as tarefas
  def listar_tarefas(self):
    if self.__lista_tarefas == []:
      print("Ainda não existem tarefas !")
    else:
      print("Tarefas:")
      for tarefa in self.__lista_tarefas:
        # para tarefas sem materia
        if tarefa.materia_correspondente == None:
          materia_correspondente = "sem materia"
          self.__tela_tarefa.mostra_dados({"nome_tarefa": tarefa.nome_tarefa, "data_prazo": tarefa.data_prazo, "horario_prazo":tarefa.horario_prazo,
        "descricao": tarefa.descricao, "materia_correspondente": materia_correspondente, "status_realizado": tarefa.status_realizado, "peso": tarefa.peso,
        "nota": tarefa.nota})
        # para tarefas com materia
        else:
          self.__tela_tarefa.mostra_dados({"nome_tarefa": tarefa.nome_tarefa, "data_prazo": tarefa.data_prazo, "horario_prazo":tarefa.horario_prazo,
        "descricao": tarefa.descricao, "materia_correspondente": tarefa.materia_correspondente.nome, "status_realizado": tarefa.status_realizado, "peso": tarefa.peso,
        "nota": tarefa.nota})

  #pega tarefa pelo seu nome
  def pega_tarefa_por_nome(self, nome: str):
    for tarefa in self.__lista_tarefas:
      if tarefa.nome_tarefa == nome:
        return tarefa
      return None

  #excluir uma tarefa
  def excluir_tarefa(self):
    self.listar_tarefas()
    nome_tarefa = self.__tela_tarefa.selecionar_tarefa()
    tarefa = self.pega_tarefa_por_nome(nome_tarefa)

    if(tarefa is not None):
      self.__lista_tarefas.remove(tarefa)
      print("Tarefa removida!")
      self.listar_tarefas()
    else:
      self.__tela_tarefa.mostra_mensagem("ATENÇÃO: Tarefa não existente")
  
  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def listar_feito(self):
    if self.__lista_tarefas == []:
      print("Ainda não existem tarefas !")
    else:
      print("Tarefas feitas:")
      for tarefa in self.__lista_tarefas:
        if tarefa.status_realizado == True:
          print(tarefa.nome_tarefa)

  def listar_a_fazer(self):
    if self.__lista_tarefas == []:
      print("Ainda não existem tarefas !")
    else:
      print("Tarefas a fazer:")
      for tarefa in self.__lista_tarefas:
        if tarefa.status_realizado == False:
          print(tarefa.nome_tarefa)

  def pegar_por_materia(self, materia):
    lista_tarefa_da_materia = []
    for tarefa in self.__lista_tarefas:
      if tarefa.materia_correspondente.codigo == materia:
        lista_tarefa_da_materia.append(tarefa)
    return lista_tarefa_da_materia

  def alterar_tarefa(self):
    if self.__lista_tarefas == []:
      print("Ainda não existem tarefas !")
    else:
      nome_da_tarefa = self.__tela_tarefa.seleciona_tarefa()
      tarefa = self.pega_tarefa_por_nome(nome_da_tarefa)

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
        self.listar_tarefas()
      else:
        self.__tela_tarefa.mostra_mensagem("ATENÇÃO: Tarefa não existente")

  def abre_tela(self):
    lista_opcoes = {1: self.adicionar_tarefa, 2: self.excluir_tarefa, 3: self.listar_tarefas, 4: self.listar_feito, 5: self.listar_a_fazer, 6: self.alterar_tarefa, 0: self.retornar}
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_tarefa.tela_opcoes()]()

  

