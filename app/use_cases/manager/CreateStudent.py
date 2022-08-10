from ...model import College, Student
from ..Base import Base


class CreateStudent(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def execute(self) -> Student:
        pass
