from ...model.Term import Term
from ..Base import Base


class SelectSection(Base):

    def __init__(self, term: Term) -> None:
        super().__init__()
        self.term = term
