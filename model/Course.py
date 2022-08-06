from .Term import Term


class Course:

    def __init__(self, name: str) -> None:
        self.term: Term = None
        self.name = name
