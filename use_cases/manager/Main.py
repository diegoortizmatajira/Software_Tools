from ..Base import Base
from .CreateProgram import CreateProgram
from .Login import Login
from ...model.College import College
from ...model.Manager import Manager


class Main(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.current_user: Manager = None
        self.college = college

    def Execute(self):
        login = Login(self.college)
        self.current_user, result = login.execute()
        if not result.ok:
            self.print_error(result.message)
        self.print(result.message)
