from persistencia.professorDAO import ProfessorDAO
from limite.tela_professor import TelaProfessor
from entidade.professor import Professor

class ControladorProfessor(): 

    def __init__(self, controlador_sistema):
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema
        self.__professores_dao = ProfessorDAO()
        self.__lista_de_professores = self.__professores_dao.get_all()

    #cadastrar um professor
    def adicionar_professor(self):
        dados_professor = self.__tela_professor.pega_dados()
        if dados_professor == None:
            return
        for professor in self.__lista_de_professores:
            if professor.nome == dados_professor["nome"]:
                self.__tela_professor.mostra_mensagem("Professor já existente!")
                return

        professor = Professor(dados_professor["nome"], dados_professor["email"], dados_professor["telefone"])
        self.__professores_dao.add(professor)
       
    
    #listar professores e seus atributos
    def listar_professores(self):
        if self.__lista_de_professores == []:
            self.__tela_professor.mostra_mensagem("Ainda não existem professores!")
            return
          
        seleciona = self.__tela_professor.seleciona_professor(self.dados_listar_professores())
        if seleciona != None:
            professor = self.pega_professor_por_id(seleciona)
            mostra_professor = self.__tela_professor.mostra_dados(professor)

    def dados_listar_professores(self):
        return [f"ID: {professor.id_professor}  Nome: {professor.nome}" for professor in self.__lista_de_professores]

    def dados_professor(self, professor):
        dados = {}
        dados["id"] = professor.id_professor
        dados["nome"] = professor.nome
        dados["email"] = professor.email
        dados["telefone"] = professor.telefone
        return dados

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
        if id == "":
            return None
        for professor in self.__lista_de_professores:
            if(professor.id_professor == id):
                return professor
        return None

    #alterar dados do professor
    def alterar_professor(self):
        if self.__lista_de_professores == []:
            self.__tela_professor.mostra_mensagem("Não há nenhum professor cadastrado ainda!")
            return

        id = self.__tela_professor.seleciona_professor(self.dados_listar_professores())
        professor = self.pega_professor_por_id(id)

        if professor != None:
            novos_dados_professor = self.__tela_professor.pega_dados()
            professor.nome = novos_dados_professor["nome"]
            professor.email = novos_dados_professor["email"]
            professor.telefone = novos_dados_professor["telefone"]
            self.__tela_professor.mostra_mensagem("Professor alterado!")
            return

        return

    #excluir professor
    def excluir_professor(self):
        if self.__lista_de_professores == []:
            self.__tela_professor.mostra_mensagem("Não existem professores!")
            return

        id = self.__tela_professor.seleciona_professor(self.dados_listar_professores())
        professor = self.pega_professor_por_id(id)

        if(professor is not None):
            self.__professores_dao.remove(professor)
            self.__tela_professor.mostra_mensagem("Professor excluído!")
            return
            
        return
              

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_professor, 2: self.excluir_professor, 3: self.listar_professores, 4: self.alterar_professor, 5: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_professor.tela_opcoes()]()