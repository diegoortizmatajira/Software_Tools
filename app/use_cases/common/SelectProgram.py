from ...model.College import College
from ..Base import Base


class SelectProgram(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college
