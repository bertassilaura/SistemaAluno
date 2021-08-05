class Materia():

    def __init__(self, nome: str, semestre: str, dia_da_semana: str, horario: str, link: str, classificacao: str, criterio_de_presenca: str, numero_avaliacoes: str):
        self.__nome = nome
        self.__semestre = semestre
        self.__dia_da_semana = dia_da_semana
        self.__horario = horario
        self.__link = link
        self.__classificacao = classificacao
        self.__criterio_de_presenca = criterio_de_presenca
        self.__numero_avaliacoes = numero_avaliacoes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def semestre(self):
        return self.__semestre
    
    @semestre.setter
    def semestre(self, semestre):
        self.__semestre = semestre

    @property
    def dia_da_semana(self):
        return self.__dia_da_semana
    
    @dia_da_semana.setter
    def dia_da_semana(self, dia_da_semana):
        return self.__dia_da_semana

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, link):
        self.__link = link

    @property
    def classificacao(self):
        return self.__classificacao

    @classificacao.setter
    def classificacao(self, classificacao):
        self.__classificacao = classificacao

    @property
    def criterio_de_presenca(self):
        return self.__criterio_de_presenca

    @criterio_de_presenca.setter
    def criterio_de_presenca(self, criterio_de_presenca):
        self.__criterio_de_presenca = criterio_de_presenca

    @property
    def numero_avaliacoes(self):
        return self.__numero_avaliacoes

    @numero_avaliacoes.setter
    def numero_avaliacoes(self, numero_avaliacoes):
        self.__numero_avaliacoes = numero_avaliacoes

