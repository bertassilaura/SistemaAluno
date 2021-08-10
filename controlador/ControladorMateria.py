from limite.TelaMateria import TelaMateria
from entidade.Materia import Materia
from controlador.ControladorSistema import ControladorSistema

class ContorladorMateria():
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_materia = TelaMateria
        self.__lista_materias = []
    
    def adicionar_materia(self):
        dados = self.__tela_materia.pega_dados()
        materia = Materia(dados['nome'], dados['professor'], dados['semestre'], dados['dia_da_semana'], 
        dados['horario'], dados['link'], dados['classificacao'], 
        dados['criterio_de_presenca'], dados['numero_avaliacoes'])
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
    
    def listar_por_professor(self, professor):
        for materia in self.__lista_materias:
            if materia.professor == professor:
                self.__tela_materia.mostra_dados({"professor": materia.professor})
                     

'''
    def listar_por_semestre():
    def listar_por_professor()
    def listar_por_dia_da_semana()
    def listar_por_semana()
    
    def abre_tela()
    def retornar()
'''
