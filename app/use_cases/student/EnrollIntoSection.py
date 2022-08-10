from ...model import College
from ..Base import Base


class EnrollIntoSection(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def execute(self):
        pass
