from .Base import Base, MenuOption
from ..model.College import College, Manager
from .manager.Main import Main as Manager_Main


class Main(Base):

    def __init__(self) -> None:
        super().__init__()
        self.college = College("Lambton College")
        self.admin = Manager("admin", "System Administrator")
        # adds a default manager
        self.college.add_manager(self.admin)

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
