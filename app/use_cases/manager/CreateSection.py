from ...model.College import College
from ...model.Section import Section
from ..Base import Base


class CreateSection(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def execute(self) -> Section:
        pass
