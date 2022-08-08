from typing import TYPE_CHECKING, List
from .Term import Term
from ..dtos.Status import Status
if TYPE_CHECKING:
    from .College import College, Status


class Program:

    def __init__(self, name: str, duration_in_years: int) -> None:
        self.college: College = None
        self.terms: List[Term] = []
        self.name = name
        self.duration_in_years = duration_in_years

    def add_term(self, term: Term) -> Status:
        if term.program != None:
            return Status(False, "The term already exists")
        term.program = self
        self.terms.append(term)
        return Status(True, "Successfully added term")
