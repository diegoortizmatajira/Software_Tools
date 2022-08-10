from ...model.College import College
from ...model.Program import Program
from ..Base import Base


class SelectProgram(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def execute(self) -> Program:
        self.header("Select an academic program")
        selection = self.list_selector(
            self.college.programs,
            f'{"Program name":50.50} {"Years":5} {"Terms":5}', lambda program:
            f'{program.name:50.50} {program.duration_in_years:>5} {len(program.terms):>5}'
        )
        if selection == None:
            self.print_warning('You have finished without selecting a program')
        else:
            self.print_success(f"You selected the program '{selection.name}'")
        return selection
