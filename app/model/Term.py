from typing import TYPE_CHECKING, List
from .Course import Course
from .Section import Section
from ..dtos.Status import Status
if TYPE_CHECKING:
    from .Program import Program


class Term:

    def __init__(self, name: str, number: int) -> None:
        self.program: Program = None
        self.courses: List[Course] = []
        self.sections: List[Section] = []
        self.name = name
        self.number = number

    def add_course(self, course: Course) -> Status:
        if course.term != None:
            return Status(False, "The course already exists")
        course.term = self
        self.courses.append(course)
        return Status(True, "Successfully added course")

    def add_section(self, section: Section) -> Status:
        if section.term != None:
            return Status(False, "The section already exists")
        section.term = self
        self.sections.append(section)
        return Status(True, "Successfully added section")
