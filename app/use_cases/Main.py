from .Base import Base, MenuOption
from ..model.College import College, Manager, Program
from .manager.Main import Main as Manager_Main


class Main(Base):

    def __init__(self) -> None:
        super().__init__()
        self.college = create_populated_college()

    def ExecuteManagerMain(self):
        use_case = Manager_Main(self.college)
        use_case.Execute()

    def ExecuteStudentMain(self):
        pass

    def execute(self):
        self.menu("Login Options",
                  MenuOption("m", "Manager Login", self.ExecuteManagerMain),
                  MenuOption("s", "Student Login", self.ExecuteStudentMain))
        self.print_success('\n\nThank you for using the system...\n')


def create_populated_college():
    college = College("Lambton College")
    admin = Manager("admin", "System Administrator")
    aimt = Program("Artificial Intelligence and Machine Learning", 2)
    ahcl = Program("Advanced Health Care Leadership", 2)
    # adds a default manager
    college.add_manager(admin)
    college.add_program(aimt)
    college.add_program(ahcl)
    return college
