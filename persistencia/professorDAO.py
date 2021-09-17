from persistencia.DAO import DAO
from entidade.professor import Professor


class ProfessorDAO(DAO):
    def __init__(self):
        super().__init__('data/professor.pkl')

    def add(self, professor: Professor):
        if professor is not None and isinstance(professor, Professor):
            super().add(professor.id_professor, professor)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
