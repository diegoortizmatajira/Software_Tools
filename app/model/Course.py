from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Term import Term


class Course:

    def __init__(self, name: str) -> None:
        self.term: Term = None
        self.name = name
