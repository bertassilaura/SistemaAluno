from limite.tela_materia import TelaMateria
from entidade.materia import Materia

class ContorladorMateria():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_materia = TelaMateria()
        self.__lista_materias = []
    
    def adicionar_materia(self):
        dados_materia = self.__tela_materia.pega_dados()
        materia = Materia(dados_materia['nome'], dados_materia['professor'], dados_materia['semestre'], dados_materia['dia_da_semana'], dados_materia['horario'], dados_materia['link'], dados_materia['classificacao'], dados_materia['criterio_de_presenca'], dados_materia['numero_avaliacoes'])
        self.__lista_materias.append(materia)

    def listar_materias(self):
        for materia in self.__lista_materias:
            self.__tela_materia.mostra_dados({"nome": materia.nome,"professor": materia.professor, "semestre": materia.semestre, "codigo": materia.codigo, "dia_da_semana": materia.dia_da_semana, "horario": materia.horario, "link": materia.link, "classificacao": materia.classificacao, "criterio_de_presenca": materia.criterio_de_presenca, "numero_avaliacoes": materia.numero_avaliacoes})
    
    def pega_materia_por_codigo(self, codigo: str):
        for materia in self.__lista_materias:
            if materia.codigo == codigo:
                return materia
            return None
  
    def excluir_materia(self):
        self.listar_materias()
        codigo_materia = self.__tela_materia.selecionar_materia()
        materia = self.pega_materia_por_codigo(codigo_materia)

        if(materia is not None):
            self.__lista_materias.remove(materia)
            self.listar_materias()

        else:
            self.__tela_materia.mostra_mensagem("ATENÇÃO: Materia não existente")
    
    def listar_por_professor(self, professor):
        for materia in self.__lista_materias:
            if materia.professor == professor:
                print(materia.professor)
    
    def listar_por_semestre(self, semestre):
        for materia in self.__lista_materias:
            if materia.semestre == semestre:
                print(materia.nome)
    
    def listar_por_semana(self, dia_da_semana):
        for materia in self.__lista_materias:
            if materia.dia_da_semana == dia_da_semana:
                print(materia.nome)
    
    def calcular_media_final(self):
        pass
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_materia, 2: self.excluir_materia, 3: self.listar_por_semestre, 4: self.listar_por_professor, 5: self.listar_por_semana, 6: self.calcular_media_final, 7: self.listar_materias, 0: self.retornar}

        continua =True
        while continua:
            lista_opcoes[self.__tela_materia.tela_opcoes()]()      


