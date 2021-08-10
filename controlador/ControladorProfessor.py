from controlador.ControladorSistema import ControladorSistema
from limite.TelaProfessor import TelaProfessor
from entidade.Professor import Professor

class ControladorProfessor():

    def __init__(self, Controlador_Sistema):
        self.__lista_de_professores = []
        self.__TelaProfessor = TelaProfessor()
        self.__ControladorSistema = ControladorSistema

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_professor, 2: self.excluir_professor, 3: self.listar_professores, 0: self.retornar()}

        continua = True
        while continua:
            lista_opcoes[self.__TelaProfessor.tela_opcoes()]()

    def adicionar_professor(self):
        dados_professor = self.__TelaProfessor.pega_dados()
        professor = Professor(dados_professor["nome"], dados_professor["email"], dados_professor["telefone"])
        self.__lista_de_professores.append(professor)

    def listar_professores(self):
        for professor in self.__lista_de_professores:
            self.__TelaProfessor.mostra_dados({"nome": professor.nome, "email": professor.email, "telefone": professor.telefone})

    def retornar(self):
        self.__ControladorSistema.abre_tela()

    def pega_professor_por_nome(self, nome: str):
        for professor in self.__lista_de_professores:
            if(professor.nome == nome):
                return professor
        return None

    def alterar_professor(self):
        self.listar_professores()
        nome_professor = self.__TelaProfessor.selecionar_professor()
        professor = self.pega_professor_por_nome(nome_professor)

        if(professor is not None):
            novos_dados_professor = self.__TelaProfessor.pega_dados()
            professor.nome = novos_dados_professor["nome"]
            professor.email = novos_dados_professor["email"]
            professor.telefone = novos_dados_professor["telefone"]
            self.listar_professores()
        else:
            self.__TelaProfessor.mostra_mensagem("ATENÇÃO: Professor não existente")

    def excluir_professor(self):
        self.listar_professores()
        nome_professor = self.__TelaProfessor.selecionar_professor()
        professor = self.pega_professor_por_nome(nome_professor)

        if(professor is not None):
            self.__lista_de_professores.remove(professor)
            self.listar_professores()
        else:
            self.__TelaProfessor.mostra_mensagem("ATENÇÃO: Professor não existente")

