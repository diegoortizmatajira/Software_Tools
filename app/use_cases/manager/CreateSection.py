from ...model import College, Section
from ..Base import Base


class CreateSection(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def execute(self) -> Section:
        pass
