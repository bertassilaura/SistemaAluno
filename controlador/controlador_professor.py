from limite.tela_professor import TelaProfessor
from entidade.professor import Professor

class ControladorProfessor(): 

    def __init__(self, controlador_sistema):
        self.__lista_de_professores = []
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    #cadastrar um professor
    def adicionar_professor(self):
        dados_professor = self.__tela_professor.pega_dados()
        for professor in self.__lista_de_professores:
            if professor.nome == dados_professor["nome"]:
                self.__tela_professor.mostra_mensagem("Professor já existente!")
                print("\n")
                return
        professor = Professor(dados_professor["nome"], dados_professor["email"], dados_professor["telefone"])
        self.__lista_de_professores.append(professor)
        self.__tela_professor.mostra_mensagem("Professor adicionado!")
        print("\n")
        self.listar_professores()

    #listar professores e seus atributos
    def listar_professores(self):
        if self.__lista_de_professores == []:
            self.__tela_professor.mostra_mensagem("Ainda não existem professores!")
            print("\n")
        else:
            self.__tela_professor.mostra_mensagem("Professores:")
            print("\n")
            for professor in self.__lista_de_professores:
                self.__tela_professor.mostra_dados({"nome": professor.nome, "email": professor.email, "telefone": professor.telefone, "id_professor": professor.id_professor})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    #pega professor por nome
    def pega_professor_por_nome(self, nome):
        for professor in self.__lista_de_professores:
            if(professor.nome == nome):
                return professor
        return None

    #pega professor por ID
    def pega_professor_por_id(self, id):
        for professor in self.__lista_de_professores:
            if(professor.id_professor == id):
                return professor
        return None

    #alterar dados do professor
    def alterar_professor(self):
        self.listar_professores()
        id = self.__tela_professor.selecionar_professor()
        professor = self.pega_professor_por_id(id)

        if(professor is not None):
            novos_dados_professor = self.__tela_professor.pega_dados()
            professor.nome = novos_dados_professor["nome"]
            professor.email = novos_dados_professor["email"]
            professor.telefone = novos_dados_professor["telefone"]
            self.__tela_professor.mostra_mensagem("Professor alterado!")
            print("\n")
            self.listar_professores()
        else:
            self.__tela_professor.mostra_mensagem("ATENÇÃO: Professor não existente")
            print("\n")

    #excluir professor
    def excluir_professor(self):
        if self.__lista_de_professores == []:
            self.__tela_professor.mostra_mensagem("Não existem professores!")
            print("\n")
        else:
            self.listar_professores()
            id = self.__tela_professor.selecionar_professor()
            professor = self.pega_professor_por_id(id)

            if(professor is not None):
                self.__lista_de_professores.remove(professor)
                self.__tela_professor.mostra_mensagem("Professor excluído!")
                print("\n")
                self.listar_professores()
            else:
                self.__tela_professor.mostra_mensagem("ATENÇÃO: Professor não existente")
                print("\n")

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_professor, 2: self.excluir_professor, 3: self.listar_professores, 4: self.alterar_professor, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_professor.tela_opcoes()]()