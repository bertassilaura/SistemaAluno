from limite.TelaMateria import TelaMateria
from entidade.Materia import Materia

class ControladorMateria():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_materia = TelaMateria
        self.__lista_materias = []
    
    def adicionar_materia(self):
        dados_materia = self.__tela_materia.pega_dados()
        materia = Materia(dados_materia['nome'], dados_materia['professor'], dados_materia['semestre'], dados_materia['dia_da_semana'], 
        dados_materia['horario'], dados_materia['link'], dados_materia['classificacao'], 
        dados_materia['criterio_de_presenca'], dados_materia['numero_avaliacoes'])
        self.__lista_materias.append(materia)

    def listar_materias(self):
        for materia in self.__lista_materias:
            self.__tela_materia.mostra_dados({"nome": materia.nome,"professor": materia.professor, "semestre": materia.semestre, 
            "dia_da_semana": materia.dia_da_semana, "horario": materia.horario, "link": materia.link, 
            "classificacao": materia.classificacao, "criterio_de_presenca": materia.criterio_de_presenca, "numero_avaliacoes": materia.numero_avaliacoes})
    
    def pega_materia_por_nome(self, nome: str):
        for materia in self.__lista_materias:
            if materia.nome == nome:
                return materia
            return None
  
    def excluir_materia(self):
        self.listar_materias()
        nome_materia = self.__tela_materia.selecionar_materia()
        materia = self.pega_materia_por_nome(nome_materia)

        if(materia is not None):
            self.__lista_materias.remove(materia)
            self.listar_materias()
        else:
            self.__tela_materia.mostra_mensagem("ATENÇÃO: Materia não existente")
    
    # Tenho duvida se esses metodos estao corretos
    def listar_por_professor(self):
        for materia in self.__lista_materias:
            self.__tela_materia.mostra_dados({"professor": materia.professor}) 
    
    def listar_por_semestre(self):
        for materia in self.__lista_materias:
            self.__tela_materia.mostra_dados({"semestre": materia.semestre})
    
    def listar_por_dia_da_semana(self):
        for materia in self.__lista_materias:
            self.__tela_materia.mostra_dados({"dia_da_semana": materia.dia_da_semana})
    
    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_materia, 2: self.excluir_materia, 3: self.listar_materias, 4: self.listar_por_professor, 
                        5:self.listar_por_semestre , 6: self.listar_por_dia_da_semana, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_materia.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
