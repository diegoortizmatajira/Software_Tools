from ..Base import Base, MenuOption
from .CreateProgram import CreateProgram
from .CreateCourse import CreateCourse
from .CreateSection import CreateSection
from .CreateStudent import CreateStudent
from .CreateTerm import CreateTerm
from . import CreateProgram
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

    def ExecuteCreateTerm(self):
        use_case = CreateTerm(self.college)
        use_case.execute()

    def ExecuteCreateCourse(self):
        use_case = CreateCourse(self.college)
        use_case.execute()

    def ExecuteCreateSection(self):
        use_case = CreateSection(self.college)
        use_case.execute()

    def ExecuteCreateStudent(self):
        use_case = CreateStudent(self.college)
        use_case.execute()

    def Execute(self):
        login = Login(self.college)
        self.current_user, result = login.execute()
        if not result.ok:
            self.print_error(result.message)
            return
        self.print_success(result.message)
        self.menu(
            "Manager Menu",
            MenuOption('p', 'Create a new Academic Program',
                       self.ExecuteCreateProgram),
            MenuOption('t', 'Create a new Term in Program',
                       self.ExecuteCreateTerm),
            MenuOption('c', 'Create a new Course in Term',
                       self.ExecuteCreateCourse),
            MenuOption('s', 'Create a new Section for a Term',
                       self.ExecuteCreateSection),
            MenuOption('r', 'Create a new Student record',
                       self.ExecuteCreateStudent),
        )
