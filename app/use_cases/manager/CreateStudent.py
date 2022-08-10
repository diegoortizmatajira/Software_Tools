from ...model.College import College
from ...model.Student import Student
from ..Base import Base


class CreateStudent(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def execute(self) -> Student:
        pass
