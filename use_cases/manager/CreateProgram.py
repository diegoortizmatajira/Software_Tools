from ..model.College import College, Program
from .Base import Base


class CreateProgram(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def collect_input(self) -> Program:
        name = input("Enter the program name:\n")
        duration_in_years = input("Enter the program duration in years:\n")
        return Program(name, duration_in_years)

    def execute(self) -> Program:
        program = self.collect_input()
        result = self.college.add_program(program)
        if not result.ok:
            self.print_error(result.message)
            return None
        self.print(result.message)
        return program
