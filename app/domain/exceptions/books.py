from dataclasses import dataclass

from config import TITLE_MAX_LENGTH
from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class TitleTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f"Слишком длинное название: {self.text[:TITLE_MAX_LENGTH]}..."


@dataclass(eq=False)
class EmptyTextException(ApplicationException):
    @property
    def message(self):
        return "Текст не может быть пустым"


@dataclass(eq=False)
class InvalidYearException(ApplicationException):
    year: int

    @property
    def message(self):
        return f"Неверное значение года: {self.year}"


@dataclass(eq=False)
class InvalidStatusException(ApplicationException):
    status: str

    @property
    def message(self):
        return f"Введен неверный статус: {self.status}"
