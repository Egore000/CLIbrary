from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Literal

from config import TITLE_MAX_LENGTH
from domain.exceptions.books import (EmptyTextException,
                                     InvalidStatusException,
                                     InvalidYearException,
                                     TitleTooLongException)
from domain.values.base import BaseValue


@dataclass
class Year(BaseValue):
    value: int

    def validate(self):
        try:
            self.value = int(self.value)
        except (TypeError, ValueError):
            raise InvalidYearException(self.value)

        if int(self.value) > datetime.now().year:
            raise InvalidYearException(self.value)

    def as_generic_type(self):
        return int(self.value)


@dataclass
class Status(BaseValue):
    value: Literal["В наличии", "Выдана"]

    def validate(self):
        if self.value not in ["В наличии", "Выдана"]:
            raise InvalidStatusException(self.value)

    def as_generic_type(self):
        return str(self.value)


@dataclass
class Text(BaseValue):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTextException()

    def as_generic_type(self):
        return str(self.value)


@dataclass
class Title(Text):
    def validate(self):
        super().validate()

        if len(self.value) > TITLE_MAX_LENGTH:
            raise TitleTooLongException(self.value)


@dataclass
class Author(Text):
    def validate(self):
        super().validate()
