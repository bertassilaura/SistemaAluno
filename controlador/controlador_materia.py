from PySimpleGUI.PySimpleGUI import main
from limite.tela_materia import TelaMateria
from entidade.materia import Materia
from persistencia.materiaDAO import MateriaDAO

class ContorladorMateria():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_materia = TelaMateria()
        self.__materia_dao = MateriaDAO()
        self.__id_materia = 0
    
    def adicionar_materia(self):
        list_box_professor = self.__controlador_sistema.controlador_professor.dados_listar_professores()
        dados_materia = self.__tela_materia.pega_dados(list_box_professor)
        if (dados_materia == None):
            return
        else:
            for materia in self.__materia_dao.get_all():
                if materia.codigo == dados_materia["codigo"]:
                    self.__tela_materia.mostra_mensagem("Uma matéria com esse código já existe!")
                    return
            if dados_materia["professor"] == "":
                professor = None
            else: 
                professor = self.__controlador_sistema.controlador_professor.pega_professor_por_id(dados_materia["professor"])
                if professor == None:
                    self.__tela_materia.mostra_mensagem("Professor não existente\nCriando matéria sem professor")
                else:
                    professor = professor.nome
            
            maior = 0
            for materia in self.__materia_dao.get_all():
                if materia.id_materia > maior:
                    maior = materia.id_materia

            self.__id_materia = maior + 1

            materia = Materia(dados_materia['nome'], dados_materia['semestre'], dados_materia["codigo"], dados_materia['dia_da_semana'], dados_materia['horario'], dados_materia['link'], dados_materia['classificacao'], dados_materia['criterio_de_presenca'], dados_materia['numero_avaliacoes'], self.__id_materia, professor)
            self.__tela_materia.mostra_mensagem("Matéria adicionada! :)")
            self.__materia_dao.add(materia)


    def listar_materias(self):
        if self.__materia_dao.get_all() == []:
            self.__tela_materia.mostra_mensagem("A lista de matérias está vazia !")
        else:
            seleciona = self.__tela_materia.selecionar_materia(self.dados_lista_materias())
            if seleciona != None:
                materia = self.pega_materia_por_id(seleciona)
                mostra_materia = self.__tela_materia.mostra_dados(materia)
                return mostra_materia
            return

#-----------PEGA MATERIA POR CODIGO---------------        
    def pega_materia_por_id(self, id):
        for materia in self.__materia_dao.get_all():
            if materia.id_materia == int(id):
                return materia
        return None
    
#-----------RETORNA CODIGO E NOME DAS MATERIAS---------------
    def dados_lista_materias(self):
        return [f'ID: {materia.id_materia} Nome: {materia.nome}' for materia in self.__materia_dao.get_all()]

#-----------EXCLUI MATERIAS---------------
    def excluir_materia(self):
        if self.__materia_dao.get_all() == []:
            self.__tela_materia.mostra_mensagem("Ainda não existem matérias !")
            return
        
        id = self.__tela_materia.selecionar_materia(self.dados_lista_materias())

        if(id is not None):
            self.__materia_dao.remove(id)
            self.__tela_materia.mostra_mensagem("Matéria excluída!")

#-----------LISTA MATERIAS POR SEMESTRE---------------  
    def listar_por_semestre(self):
        if self.__materia_dao.get_all() == []:
            self.__tela_materia.mostra_mensagem("Ainda não existem matérias!")
        else:
            qual_semestre = self.__tela_materia.semestres()
            existe = 0
            lista = []
            for materia in self.__materia_dao.get_all():
                if materia.semestre == qual_semestre:
                    existe = 1
                    lista += [f'Código: {materia.codigo} | Nome: {materia.nome} | Semestre: {materia.semestre}']
            if existe == 1:
                self.__tela_materia.mostra_lista(lista)
            else:
                self.__tela_materia.mostra_mensagem("Nenhuma matéria nesse semestre.")

#-----------LISTA MATERIAS POR DIA DA SEMANA--------------- 
    def listar_por_dia_da_semana(self):
        if self.__materia_dao.get_all() == []:
            self.__tela_materia.mostra_mensagem("Ainda não existem matérias!")
        else:
            qual_dia = self.__tela_materia.dias_da_semana()
            existe = 0
            lista = []
            for materia in self.__materia_dao.get_all():
                if materia.dia_da_semana == qual_dia:
                    existe = 1
                    lista += [f'Código: {materia.codigo} | Nome: {materia.nome} | Dia da semana: {materia.dia_da_semana}']
            if existe == 1:
                self.__tela_materia.mostra_lista(lista)
            else:
                self.__tela_materia.mostra_mensagem("Nenhuma matéria nesse dia.")

#-----------CALCULA MEDIA FINAL DE UMA MATERIA---------------    
    def calcular_media_final(self): 
        if self.__materia_dao.get_all() == []:
            self.__tela_materia.mostra_mensagem("Ainda não existem matérias!")
        else:
            nota_total = 0
            peso_total = 0
            
            id = self.__tela_materia.selecionar_materia(self.dados_lista_materias())
            materia = self.pega_materia_por_id(id)

            if materia == None:
                self.__tela_materia.mostra_mensagem("Não existe matéria com esse ID!")
                return
            
            tarefas_materia = self.__controlador_sistema.controlador_tarefa.pegar_por_materia(id)

            if tarefas_materia == None:
                self.__tela_materia.mostra_mensagem("Não existem tarefas dessa matéria")
                return

            for tarefa in tarefas_materia:
                nota_total += float(tarefa.nota) * float(tarefa.peso)
                peso_total += float(tarefa.peso)

            media_final = nota_total / peso_total
            self.__tela_materia.mostra_mensagem(f"Sua nota final na matéria desejada é {media_final:.2f}")
    
#-----------ALTERA MATERIAS---------------
    def alterar_materia(self):
        if self.__materia_dao.get_all() == []:
            self.__tela_materia.mostra_mensagem("Ainda não existem matérias!")
            return
            
        id = self.__tela_materia.selecionar_materia(self.dados_lista_materias())
        materia = self.pega_materia_por_id(id)
        list_box_professor = self.__controlador_sistema.controlador_professor.dados_listar_professores()

        if(materia is not None):
            novos_dados_materia = self.__tela_materia.pega_dados(list_box_professor)
            if novos_dados_materia != None:
                materia.nome = novos_dados_materia["nome"]
                materia.semestre = novos_dados_materia["semestre"]
                materia.professor = novos_dados_materia["professor"]
                materia.codigo = novos_dados_materia["codigo"]
                materia.dia_da_semana = novos_dados_materia["dia_da_semana"]
                materia.horario = novos_dados_materia["horario"]
                materia.link = novos_dados_materia["link"]
                materia.classificacao = novos_dados_materia["classificacao"]
                materia.criterio_de_presenca = novos_dados_materia["criterio_de_presenca"]
                materia.numero_avaliacoes = novos_dados_materia["numero_avaliacoes"]
                self.__tela_materia.mostra_mensagem("Matéria alterada!")
                self.__materia_dao.add(materia)
                return
            return

#-----------RETORNA---------------
    def retornar(self):
        self.__controlador_sistema.abre_tela()

#-----------ABRE TELA---------------
    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_materia, 2: self.excluir_materia, 3: self.listar_por_semestre, 4: self.calcular_media_final, 5: self.listar_materias, 6: self.alterar_materia, 7: self.listar_por_dia_da_semana, 8: self.retornar}

        continua =True
        while continua:
            lista_opcoes[self.__tela_materia.tela_opcoes()]()