from ..Base import Base
from ...model.College import College, Manager
from ...dtos.Status import Status
from typing import Tuple


class Login(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college
        self.remaining_attempts = 3

    def ask_credentials(self):
        self.header('Welcome to the Student Enrollment System')
        manager_username = self.input("Enter the manager username: ")
        self.remaining_attempts = self.remaining_attempts - 1
        return self.college.get_manager_by_username(manager_username)

    def execute(self) -> Tuple[Manager, Status]:
        while self.remaining_attempts > 0:
            manager = self.ask_credentials()
            if manager != None:
                return manager, Status(True, "Login Succeeded")
            if self.remaining_attempts > 0:
                self.print_warning("Invalid username, try again...")
        return None, Status(False, "Login Failed after multiple attempts")
