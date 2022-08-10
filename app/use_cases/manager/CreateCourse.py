from ...model.College import College
from ...model.Course import Course
from ..Base import Base


class CreateCourse(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def execute(self) -> Course:
        pass
