Implementação de telas com PySimpleGUI de um sistema orientado a objetos em python para a organização semestral do aluno

Leonardo De Brida - Atribuição de Implementação: Controlador Tarefa, Tela Tarefa, ControladorMateria, TelaMateria

Tela tarefa:
    O que falta:
        Listar tarefas e ter a opcao de selecionar e entrar para ver detalhes --------- Ok
        Tratamento de numeros recebidos na criação ou alteração de tarefa --------- OK 
        Consertar um erro que ta dando quando desisto de criar uma materia, ou excluir uma materia ------- OK

        Fazer receber peso como float -------- ok
        Arrumar mostra dados ------ ok
        Arrumar tarefas feitas e nao feitas ------ ok
        Retornar, esta dando um KeyError: '00' --------- OK

Tela Materia:
    O que falta:
        Arrumar o cancelar e retornar do alterar materia -------ok
        Listar por semestre, tratamento caso nao tenha semestre -------- ok
        Arrumar texto nos botões de entrada ---------OK
        Mostrar dados de materia ---------OK
        Colocar textos padrão nos inputs -------OK
        Arrumar tamanho do pop up de mensagens ----------OK
        Arrumar o listar materia para selecionar e mostrar ( igual fiz com o tarefa) -------OK
        retirar mensagens desnecessarias de materia --------OK

TarefaDAO:
    Ta tudo Ok

MateriaDAO:
    Alterar materia ta bugado - alteração nao se mantem na persistência; quando
    o self.__materia_dao.add(materia) é adicionado no alterar, buga mais ainda

