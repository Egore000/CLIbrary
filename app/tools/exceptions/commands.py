from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class EmptyCommandException(ApplicationException):
    @property
    def message(self):
        return "Команда не введена"
    

@dataclass(eq=False)
class UnknownCommandException(ApplicationException):
    command: str

    @property
    def message(self):
        return f"Неизвестная команда: {self.command}"
