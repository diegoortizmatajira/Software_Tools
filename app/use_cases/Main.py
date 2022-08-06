from .Base import Base
from ..model.College import College, Manager
from .manager.Main import Main as Manager_Main


class Main(Base):

    def __init__(self) -> None:
        super().__init__()
        self.college = College("Lambton College")
        self.admin = Manager("admin", "System Administrator")
        # adds a default manager
        self.college.add_manager(self.admin)

    def execute(self):
        main = Manager_Main(self.college)
        main.Execute()
