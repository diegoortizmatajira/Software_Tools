from .Base import Base, MenuOption
from ..model import College
from .manager.Main import Main as Manager_Main
from .student.Main import Main as Student_Main


class Main(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def ExecuteManagerMain(self):
        use_case = Manager_Main(self.college)
        use_case.Execute()

    def ExecuteStudentMain(self):
        use_case = Student_Main(self.college)
        use_case.Execute()

    def execute(self):
        self.menu("Login Options",
                  MenuOption("m", "Manager Login", self.ExecuteManagerMain),
                  MenuOption("s", "Student Login", self.ExecuteStudentMain))
        self.print_success('\n\nThank you for using the system...\n')
