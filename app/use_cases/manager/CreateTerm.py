from ...model import College, Term
from ..Base import Base
from ..common.SelectProgram import SelectProgram


class CreateTerm(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def execute(self) -> Term:
        programSelectionUseCase = SelectProgram(self.college)
        programSelectionUseCase.execute()
