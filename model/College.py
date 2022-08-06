from .Manager import Manager
from .Program import Program
from .Student import Student
from ..dtos.Status import Status
from typing import List


class College:

    def __init__(self, name: str) -> None:
        self.name = name
        self.managers: List[Manager] = []
        self.programs: List[Program] = []
        self.students: List[Student] = []
        # adds a default manager
        self.add_manager(Manager("admin"))

    def add_manager(self, new_manager: Manager) -> Status:
        if new_manager.college != None:
            return Status(False, "The manager already exists")
        new_manager.college = self
        self.managers.append(new_manager)
        return Status(True, "Successfully added manager")

    def add_student(self, new_student: Student) -> Status:
        if new_student.college != None:
            return Status(False, "The student already exists")
        new_student.college = self
        self.students.append(new_student)
        return Status(True, "Successfully added student")

    def add_program(self, new_program: Program) -> Status:
        if new_program.college != None:
            return Status(False, "The program already exists")
        new_program.college = self
        self.programs.append(new_program)
        return Status(True, "Successfully added program")
