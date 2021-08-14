from entidade.professor import Professor
from limite.tela_materia import TelaMateria
from entidade.materia import Materia

class ContorladorMateria():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_materia = TelaMateria()
        self.__lista_materias = []
    
    def adicionar_materia(self):
        dados_materia = self.__tela_materia.pega_dados()
        dados_professor = self.adicionar_professor_a_materia()
        materia = Materia(dados_materia['nome'], dados_professor["professor"], dados_materia['semestre'], dados_materia["codigo"], dados_materia['dia_da_semana'], dados_materia['horario'], dados_materia['link'], dados_materia['classificacao'], dados_materia['criterio_de_presenca'], dados_materia['numero_avaliacoes'])
        self.__lista_materias.append(materia)
        print("Matéria criada!")
        print("\n")
    
    # Adicionar metodo ao diagrama
    def adicionar_professor_a_materia(self):
        print("\n")
        print("Escolha 1 ou 2 para que a Materia tenha um Professor:")
        print("1 - Adicionar(criar) um Professor e inclui-lo na matéria")
        print("2 - Selecionar um já existente para inclui-lo na matéria")
        opcao = int(input("Digite a opção escolhida:"))
        if opcao == 1:
            add_professor = self.__controlador_sistema.controlador_professor.adicionar_professor()
            professor = self.__controlador_sistema.controlador_professor.pega_professor_por_nome()
        elif opcao == 2:
            professor = self.__controlador_sistema.controlador_professor.pega_professor_por_nome()

        return {"professor": professor}

    def listar_materias(self):
        for materia in self.__lista_materias:
            return self.__tela_materia.mostra_dados({"nome": materia.nome, "professor": materia.professor, "semestre": materia.semestre, "codigo": materia.codigo, "dia_da_semana": materia.dia_da_semana, "horario": materia.horario, "link": materia.link, "classificacao": materia.classificacao, "criterio_de_presenca": materia.criterio_de_presenca, "numero_avaliacoes": materia.numero_avaliacoes})
        print("\n")

    def pega_materia_por_codigo(self, codigo: str):
        for materia in self.__lista_materias:
            if materia.codigo == codigo:
                return materia

        print("Não existe uma matéria com esse código!")
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
    
    def listar_por_semestre(self):
        qual_semestre = str(input("Digite o semestre desejado: "))
        for materia in self.__lista_materias:
            if materia.semestre == qual_semestre:
                print(materia.nome)
    
    def listar_por_dia_da_semana(self):
        qual_dia = str(input("Digite o dia da semana desejado: "))
        for materia in self.__lista_materias:
            if materia.dia_da_semana == qual_dia:
                print(materia)

    def calcular_media_final(self):
        #materia = self.__controlador_sistema
        nota_total = 0
        peso_total = 0
        for materia in self.__lista_materias:
            nota_total += materia.nota
            peso_total += materia.peso

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_materia, 2: self.excluir_materia, 3: self.listar_por_semestre, 4: self.calcular_media_final, 5: self.listar_materias, 0: self.retornar}

        continua =True
        while continua:
            lista_opcoes[self.__tela_materia.tela_opcoes()]()
