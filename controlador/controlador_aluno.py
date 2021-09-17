from limite.tela_aluno import TelaAluno
from entidade.aluno import Aluno
from persistencia.alunoDAO import AlunoDAO

class ControladorAluno():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_aluno = TelaAluno()
        self.__aluno_dao = AlunoDAO()
    
    def pega_primeiro_aluno(self):
        teste = self.__aluno_dao.get_all()
        value_iterator = iter(teste)
        return next(value_iterator)

    #cria um aluno
    def criar_aluno(self):
        if len(self.__aluno_dao.get_all()) != 0:
            self.__tela_aluno.mostra_mensagem("Você já possui um cadastro!")
            return
        
        dados_aluno = self.__tela_aluno.pega_dados()
        if dados_aluno == None:
            return
        self.__aluno_dao.add(Aluno(dados_aluno["nome"], dados_aluno["email"], dados_aluno["matricula"]))
        self.__tela_aluno.mostra_mensagem("Cadastrado com sucesso!")

    #altera o aluno
    def alterar_aluno(self):

        if len(self.__aluno_dao.get_all()) != 0:
            aluno = self.pega_primeiro_aluno()
            novos_dados_aluno = self.__tela_aluno.pega_dados()
            if novos_dados_aluno != None:
                aluno.nome = novos_dados_aluno["nome"]
                aluno.email = novos_dados_aluno["email"]
                aluno.matricula = novos_dados_aluno["matricula"]
                self.__tela_aluno.mostra_mensagem("Aluno alterado!")
                self.__aluno_dao.add(aluno)
                return

        else:
            self.__tela_aluno.mostra_mensagem("Você ainda não possui um cadastro!")
            return

    #mostra os dados do aluno
    def mostra_aluno(self):

        if len(self.__aluno_dao.get_all()) != 0:
            aluno = self.pega_primeiro_aluno()
            return self.__tela_aluno.mostra_dados({"nome": aluno.nome, "email": aluno.email, "matricula": aluno.matricula})
        
        else:
            self.__tela_aluno.mostra_mensagem("Você ainda não possui um cadastro!")
            return

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_aluno, 2: self.mostra_aluno, 3: self.alterar_aluno, 4: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
