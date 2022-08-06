from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .College import College


class Manager:

    def __init__(self, username: str, fullname: str) -> None:
        self.college: College = None
        self.username = username
        self.fullname = fullname
