from db.init import library
from domain.entities.books import Book
from domain.exceptions.books import InvalidInputException
from domain.values.base import BaseValue
from domain.values.books import Author, Status, Title, Year
from tools.exceptions.commands import InvalidSearchModeException
from tools.messages import Message


def greetings():
    """Приветственное сообщение при входе в терминал программы"""

    print(Message.greeting)


def input_value(VT: BaseValue) -> BaseValue:
    """Повторяющийся ввод параметра до тех пор, пока не
    будет введено корректное значение

    :param BaseValue VT: Тип вводимого значения

    :return: Корректно введенное значение
    :rtype: BaseValue
    """

    value: BaseValue = None
    msg = getattr(Message, VT.__name__.lower())
    while not value:
        try:
            value = VT(input(msg))
        except InvalidInputException as exception:
            print(Message.error, exception.message)
    return value


def input_book_data() -> Book:
    """Ввод параметров книги и создание объекта книги

    :return: Книга с введенными параметрами
    :rtype: Book
    """

    title = input_value(Title)
    author = input_value(Author)
    year = input_value(Year)
    status = input_value(Status)

    return Book(title=title, author=author, year=year, status=status)


def find_books() -> list[Book]:
    """Поиск книг с выбором режима поиска
    по ID, по названию, по автору или по году.

    :return: Найденные книги
    :rtype: list[Book]

    :raises InvalidSearchModeException: Выбран неверный режим поиска
    """

    mode = input(Message.mode)

    match mode:
        case "1":
            id = input(Message.id)
            books = [library.get(id=id)]

        case "2":
            title = Title(input(Message.title))
            books = [library.get(title=title)]

        case "3":
            author = Author(input(Message.author))
            books = library.filter(author=author)

        case "4":
            year = Year(int(input(Message.year)))
            books = library.filter(year=year)

        case _:
            raise InvalidSearchModeException

    return books
