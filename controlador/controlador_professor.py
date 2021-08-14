from limite.tela_professor import TelaProfessor
from entidade.professor import Professor

class ControladorProfessor():

    def __init__(self, controlador_sistema):
        self.__lista_de_professores = []
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    #Cadastrar um professor
    def adicionar_professor(self):
        dados_professor = self.__tela_professor.pega_dados()
        professor = Professor(dados_professor["nome"], dados_professor["email"], dados_professor["telefone"])
        self.__lista_de_professores.append(professor)

    #listar professores e seus atributos
    def listar_professores(self):
        print(self.__lista_de_professores)
        for professor in self.__lista_de_professores:
            self.__tela_professor.mostra_dados({"nome": professor.nome, "email": professor.email, "telefone": professor.telefone})

    #retornar
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    #pega professor por nome
    def pega_professor_por_nome(self):
        nome = self.__tela_professor.selecionar_professor()
        for professor in self.__lista_de_professores:
            if(professor.nome == nome):
                return professor
        return None

    #alterar dados do professor
    def alterar_professor(self):
        nome_professor = self.__tela_professor.selecionar_professor()
        professor = self.pega_professor_por_nome(nome_professor)

        if(professor is not None):
            novos_dados_professor = self.__tela_professor.pega_dados()
            professor.nome = novos_dados_professor["nome"]
            professor.email = novos_dados_professor["email"]
            professor.telefone = novos_dados_professor["telefone"]
            self.listar_professores()
        else:
            self.__tela_professor.mostra_mensagem("ATENÇÃO: Professor não existente")

    #excluir professor
    def excluir_professor(self):
        self.listar_professores()
        nome_professor = self.__tela_professor.selecionar_professor()
        professor = self.pega_professor_por_nome(nome_professor)

        if(professor is not None):
            self.__lista_de_professores.remove(professor)
            self.listar_professores()
        else:
            self.__tela_professor.mostra_mensagem("ATENÇÃO: Professor não existente")

    #abre tela de opçoes professor
    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_professor, 2: self.excluir_professor, 3: self.listar_professores, 4: self.alterar_professor, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_professor.tela_opcoes()]()
