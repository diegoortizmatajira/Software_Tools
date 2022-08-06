from datetime import date
from typing import List
from .Term import Term
from .Student import Student
from ..dtos.Status import Status


class Section:

    def __init__(self, name: str, start_date: date, end_date: date,
                 total_seats: int) -> None:
        self.term: Term = None
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.students: List[Student] = []

    def add_student(self, student: Student) -> Status:
        # checks if there are available seats
        if self.available_seats == 0:
            return Status(
                False,
                f"There are not available seats in the section {self.name}")

        # if the student is already in other section, then remove it
        if student.current_section != None:
            student.current_section.remove_student(student)

        # adds the student and updates the available seats
        self.students.append(student)
        self.available_seats = self.available_seats - 1
        student.current_section = self
        return Status(True, f"Successfully added the student to section {self.name}")

    def remove_student(self, student: Student):
        # if the student is actually in this section, then remove it
        if student.current_section == self:
            student.current_section = None
            self.available_seats = self.available_seats + 1
