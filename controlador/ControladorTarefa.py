from limite.TelaTarefa import TelaTarefa
from entidade.Tarefa import Tarefa

class ControladorTarefa():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_tarefa = TelaTarefa
        self.__lista_tarefas = []
    
    def adicionar_tarefa(self):
        dados_tarefa = self.__tela_tarefa.pega_dados()
        tarefa = Tarefa(dados_tarefa["nome_tarefa"], dados_tarefa["data_prazo"], dados_tarefa["horario_prazo"],
                        dados_tarefa["descricao"], dados_tarefa["materia_correspondente"], dados_tarefa["status_realizado"],
                        dados_tarefa["nota"])
        self.__lista_tarefas.append(tarefa)
    
    def listar_tarefas(self):
        for tarefa in self.__lista_tarefas:
            self.__tela_tarefa.mostra_dados({"nome_tarefa": tarefa.nome_tarefa, "data_prazo": tarefa.data_prazo, "horario_prazo":tarefa.horario_prazo,
            "descricao": tarefa.descricao, "materia_correspondente": tarefa.materia_correspondente, "status_realizado": tarefa.status_realizado,
            "nota": tarefa.nota})

    def pega_tarefa_por_nome(self, nome_tarefa: str):
        for tarefa in self.__lista_tarefas:
            if tarefa.nome_tarefa == nome_tarefa:
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
    
    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_tarefa, 2: self.excluir_tarefa, 3: self.listar_tarefas, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_tarefa.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

'''
listar_feito
listar_a_fazer
listar_por_materia
listar_da_semana
'''