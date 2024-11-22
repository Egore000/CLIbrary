from dataclasses import dataclass

from config import TITLE_MAX_LENGTH
from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class InvalidInputException(ApplicationException):
    @property
    def message(self):
        return "Некорректный ввод"
    

@dataclass(eq=False)
class TitleTooLongException(InvalidInputException):
    text: str

    @property
    def message(self):
        return f"Слишком длинное название: {self.text[:TITLE_MAX_LENGTH]!r}..."


@dataclass(eq=False)
class EmptyTextException(InvalidInputException):
    @property
    def message(self):
        return "Текст не может быть пустым"


@dataclass(eq=False)
class InvalidYearException(InvalidInputException):
    year: int

    @property
    def message(self):
        return f"Неверное значение года: {self.year!r}"


@dataclass(eq=False)
class InvalidStatusException(InvalidInputException):
    status: str

    @property
    def message(self):
        return f"Введен неверный статус: {self.status!r}"
