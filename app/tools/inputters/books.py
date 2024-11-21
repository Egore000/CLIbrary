
from domain.exceptions.books import EmptyTextException, InvalidStatusException, InvalidYearException, TitleTooLongException
from domain.values.books import Author, Status, Title, Year
from tools.inputters.base import Inputter


class TitleInputter(Inputter):
    value_type = Title
    msg = ">> Название: "
    exceptions = (TitleTooLongException, EmptyTextException)


class AuthorInputter(Inputter):
    value_type = Author
    msg = ">> Автор: "
    exceptions = EmptyTextException


class YearInputter(Inputter):
    value_type = Year
    msg = ">> Год: "
    exceptions = InvalidYearException


class StatusInputter(Inputter):
    value_type = Status
    msg = ">> Статус (В наличии/Выдана): "
    exceptions = InvalidStatusException
