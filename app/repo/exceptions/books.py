from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class ObjectNotFoundException(ApplicationException):
    @property
    def message(self):
        return f"Объект не найден"
