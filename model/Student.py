from .College import College
from .Section import Section

class Student:

    def __init__(self, student_id: str, full_name: str) -> None:
        self.college: College = None
        self.current_section: Section = None
        self.student_id = student_id
        self.full_name = full_name
