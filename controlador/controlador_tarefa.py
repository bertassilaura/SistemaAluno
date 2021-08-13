from limite.tela_tarefa import TelaTarefa
from entidade.tarefa import Tarefa

class ControladorTarefa():
  
  def __init__(self, controlador_sistema):
    self.__lista_tarefas = []
    self.__tela_tarefa = TelaTarefa()
    self.__controlador_sistema = controlador_sistema

  def adicionar_tarefa(self):
    dados_tarefa = self.__tela_tarefa.pega_dados()
    #Fazer tratamento dos dados, selecionar matéria a partir de string recebida
    #Como eu preciso acessar um método de outro controlador, eu uso o atributo do controlador sistema para chegar no controlador matéria, assim usando o seu método
    materia_correspondente = self.__controlador_sistema.controlador_materia.pega_materia_por_codigo(dados_tarefa["materia_correspondente"])
    tarefa = Tarefa(dados_tarefa["nome_tarefa"], dados_tarefa["data_prazo"], dados_tarefa["horario_prazo"], dados_tarefa["descricao"], materia_correspondente, dados_tarefa["status_realizado"], dados_tarefa["peso"], dados_tarefa["nota"])
    self.__lista_tarefas.append(tarefa)
  
  def listar_tarefas(self):
    for tarefa in self.__lista_tarefas:
      self.__tela_tarefa.mostra_dados({"nome_tarefa": tarefa.nome_tarefa, "data_prazo": tarefa.data_prazo, "horario_prazo":tarefa.horario_prazo,
      "descricao": tarefa.descricao, "materia_correspondente": tarefa.materia_correspondente, "status_realizado": tarefa.status_realizado,
      "nota": tarefa.nota})

  def pega_tarefa_por_nome(self, nome: str):
    for tarefa in self.__lista_tarefas:
      if tarefa.nome == nome:
        return tarefa
      return None

  def excluir_tarefa(self):
    self.listar_tarefas()
    nome_tarefa = self.__tela_tarefa.selecionar_tarefa()
    tarefa = self.pega_tarefa_por_nome(nome_tarefa)

    if(tarefa is not None):
      self.__lista_tarefas.remove(tarefa)
      self.listar_tarefas()
    else:
      self.__tela_tarefa.mostra_mensagem("ATENÇÃO: Tarefa não existente")
  
  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def listar_feito(self):
    for tarefa in self.__lista_tarefas:
      if tarefa.status_realizado == True:
        print(tarefa)

  def listar_a_fazer(self):
    for tarefa in self.__lista_tarefas:
      if tarefa.status_realizado == False:
        print(tarefa)

  def abre_tela(self):
    lista_opcoes = {1: self.adicionar_tarefa, 2: self.excluir_tarefa, 3: self.listar_tarefas, 4: self.listar_feito, 5: self.listar_a_fazer, 0: self.retornar}
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_tarefa.tela_opcoes()]()

  

