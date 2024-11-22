from db.init import library
from domain.entities.books import Book
from domain.values.books import Author, Title, Year
from tools.exceptions.commands import InvalidSearchModeException
from tools.messages import Message 


def greetings():
    """Приветственное сообщение при входе в терминал программы"""

    print(Message.greeting)


def input_book_data() -> Book:
    """Ввод параметров книги и создание объекта книги

    :return: Книга с введенными параметрами
    :rtype: Book

    :raises TitleTooLongException: Введено слишком длинное название
    :raises EmptyTextException: Введен пустой текст
    :raises InvalidYearException: Введено неверное значение года
    :raises InvalidStatusException: Введен неверный статус
    """

    title = input(Message.title)
    author = input(Message.author)
    year = int(input(Message.year))
    status = input(Message.status)

    return Book(title=title, author=author, year=year, status=status)


def find_book() -> Book | None:
    """Поиск книги с выбором режима поиска
    по ID, по названию, по автору или по году.

    :return: Найденная книга
    :rtype: Book or None

    :raises InvalidSearchModeException: Выбран неверный режим поиска
    """

    mode = input(Message.mode)

    match mode:
        case "1":
            id = input(Message.id)
            book = library.get(id=id)

        case "2":
            title = Title(input(Message.title))
            book = library.get(title=title)

        case "3":
            author = Author(input(Message.author))
            book = library.filter(author=author)

            if book:
                book = book[0]

        case "4":
            year = Year(int(input(Message.year)))
            book = library.filter(year=year)

            if book:
                book = book[0]

        case _:
            raise InvalidSearchModeException

    return book
