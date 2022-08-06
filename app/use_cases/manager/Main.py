from ..Base import Base, MenuOption
from .CreateProgram import CreateProgram
from .Login import Login
from ...model.College import College
from ...model.Manager import Manager


class Main(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.current_user: Manager = None
        self.college = college

    def ExecuteCreateProgram(self):
        use_case = CreateProgram(self.college)
        use_case.execute()

    def Execute(self):
        login = Login(self.college)
        self.current_user, result = login.execute()
        if not result.ok:
            self.print_error(result.message)
            return
        self.print(result.message)
        self.menu(
            MenuOption('p', 'Create a new Program', self.ExecuteCreateProgram))
