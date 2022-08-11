from ...model import College, Term
from ..Base import Base
from ..common.SelectProgram import SelectProgram


class CreateTerm(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def execute(self) -> Term:
        programSelectionUseCase = SelectProgram(self.college)
        program = programSelectionUseCase.execute()
        if program == None:
            return None
        name = self.input("Please enter the name for the term: ")
        term_number = self.input("Please enter the term number: ")
        term = Term(name, term_number)
        program.add_term(term)
        self.print_success(f"Successfully created term '{term.name}'")
        return Term

