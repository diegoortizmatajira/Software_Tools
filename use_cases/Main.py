from .Base import Base
from ..model.College import College
from .manager.Main import Main as Manager_Main


class Main(Base):

    def __init__(self) -> None:
        super().__init__()
        self.college = College("Lambton College")

    def execute(self):
        main = Manager_Main(self.college)
        main.Execute()
