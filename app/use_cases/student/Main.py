from ..Base import Base, MenuOption
from .EnrollIntoSection import EnrollIntoSection
from .Login import Login
from ...model.College import College
from ...model.Student import Student


class Main(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.current_user: Student = None
        self.college = college

    def ExecuteEnrollIntoSection(self):
        use_case = EnrollIntoSection(self.college)
        use_case.execute()

    def Execute(self):
        login = Login(self.college)
        self.current_user, result = login.execute()
        if not result.ok:
            self.print_error(result.message)
            return
        self.print_success(result.message)
        self.menu(
            "Student Menu",
            MenuOption('e', 'Enroll into a Section',
                       self.ExecuteEnrollIntoSection))
