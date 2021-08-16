#from controlador.controlador_sistema import ControladorSistema
from limite.tela_materia import TelaMateria
from entidade.materia import Materia

class ContorladorMateria():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_materia = TelaMateria()
        self.__lista_materias = []
    
    def adicionar_materia(self):
        dados_materia = self.__tela_materia.pega_dados()
        if dados_materia["professor"] == "":
            print("Criando uma matéria sem professor")
            print("\n")
        else:
            print("Criando uma matéria com professor")
            print("\n")

        professor = self.__controlador_sistema.controlador_professor.pega_professor_por_nome(dados_materia["professor"])
        materia = Materia(dados_materia['nome'], dados_materia['semestre'], dados_materia["codigo"], dados_materia['dia_da_semana'], dados_materia['horario'], dados_materia['link'], dados_materia['classificacao'], dados_materia['criterio_de_presenca'], dados_materia['numero_avaliacoes'], professor)
        print("Matéria adicionada! :)")
        print("\n")
        self.__lista_materias.append(materia)

    def listar_materias(self):
        if self.__lista_materias == []:
            print("Ainda não existem matérias !")
            print("\n")
        else:
            print("Matérias:")
            print("\n")
            for materia in self.__lista_materias:
                if materia.professor == None:
                    #mostra dados com "sem professor" no campo professor
                    professor = "sem professor"
                    self.__tela_materia.mostra_dados({"nome": materia.nome, "professor": professor, "semestre": materia.semestre, "codigo": materia.codigo, "dia_da_semana": materia.dia_da_semana, "horario": materia.horario, "link": materia.link, "classificacao": materia.classificacao, "criterio_de_presenca": materia.criterio_de_presenca, "numero_avaliacoes": materia.numero_avaliacoes})
                else:
                    self.__tela_materia.mostra_dados({"nome": materia.nome, "professor": materia.professor.nome, "semestre": materia.semestre, "codigo": materia.codigo, "dia_da_semana": materia.dia_da_semana, "horario": materia.horario, "link": materia.link, "classificacao": materia.classificacao, "criterio_de_presenca": materia.criterio_de_presenca, "numero_avaliacoes": materia.numero_avaliacoes})
                
    def pega_materia_por_codigo(self, codigo: str):
        for materia in self.__lista_materias:
            if materia.codigo == codigo:
                return materia

        print("Não existe uma matéria com esse código!")
        print("\n")
        return None
  
    def excluir_materia(self):
        if self.__lista_materias == []:
            print("Ainda não existem matérias !")
            print("\n")
        else:
            self.listar_materias()
            codigo_materia = self.__tela_materia.selecionar_materia()
            materia = self.pega_materia_por_codigo(codigo_materia)

            if(materia is not None):
                self.__lista_materias.remove(materia)
                print("Matéria excluída!")
                print("\n")
                self.listar_materias()

            else:
                self.__tela_materia.mostra_mensagem("ATENÇÃO: Materia não existente")
                print("\n")
    
    def listar_por_semestre(self):
        if self.__lista_materias == []:
            print("Ainda não existem matérias!")
            print("\n")
        else:
            qual_semestre = str(input("Digite o semestre desejado: "))
            print("\n")
            existe = 0
            print("Matérias do semestre desejado:")
            print("\n")
            for materia in self.__lista_materias:
                if materia.semestre == qual_semestre:
                    existe = 1
                    print(materia.nome)
            if existe == 0:
                print("Não foi encontrada nenhuma matéria nesse semestre.")
                print("\n")
    
    def listar_por_dia_da_semana(self):
        qual_dia = str(input("Digite o dia da semana desejado [seg/ter/qua/qui/sex]: "))
        existe = 0
        for materia in self.__lista_materias:
            if materia.dia_da_semana == qual_dia:
                existe = 1
                print(materia.nome)
        if existe == 0:
            print("Não foi encontrada nenhuma matéria nesse dia.")
            print("\n")
            
    def calcular_media_final(self):
        codigo_materia = str(input("Digite o código da matéria desejada: "))
        nota_total = 0
        peso_total = 0

        tarefas_materia = self.__controlador_sistema.controlador_tarefa.pegar_por_materia(codigo_materia)

        for tarefa in tarefas_materia:
            nota_total += tarefa.nota * tarefa.peso
            peso_total += tarefa.peso

        media_final = nota_total / peso_total
        print(f"Sua nota final na matéria desejada é {media_final:.2f}")
        print("\n")
    
    def alterar_materia(self):
        codigo_da_materia = self.__tela_materia.selecionar_materia()
        materia = self.pega_materia_por_codigo(codigo_da_materia)

        if(materia is not None):
            novos_dados_materia = self.__tela_materia.pega_dados()
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
            print("Matéria alterada!")
            print("\n")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_materia, 2: self.excluir_materia, 3: self.listar_por_semestre, 4: self.calcular_media_final, 5: self.listar_materias, 6: self.alterar_materia, 7: self.listar_por_dia_da_semana, 0: self.retornar}

        continua =True
        while continua:
            lista_opcoes[self.__tela_materia.tela_opcoes()]()
