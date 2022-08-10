from ...model.Program import Program
from ..Base import Base


class SelectTerm(Base):

    def __init__(self, program: Program) -> None:
        super().__init__()
        self.program = program
