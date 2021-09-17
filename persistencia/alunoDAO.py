from persistencia.DAO import DAO
from entidade.aluno import Aluno


class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('data/aluno.pkl')

    def add(self, aluno: Aluno):
        if aluno is not None and isinstance(aluno, Aluno):
            super().add(aluno.nome, aluno)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
