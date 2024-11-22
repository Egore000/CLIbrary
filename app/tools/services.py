from db.init import library
from domain.entities.books import Book
from domain.values.books import Author, Title, Year
from tools.exceptions.commands import InvalidSearchModeException


def greetings():
    """Приветственное сообщение при входе в терминал программы"""

    print(
        """
            <<<     CLIbrary    >>>
    
Чтобы начать работу, ознакомься со списком команд:
1) get - найти нужную книгу по названию, автору или году.
2) all - вывести все имеющиeся книги.
3) add - добавить книгу.
4) delete - удалить книгу.
5) status - изменить статус книги.
6) help - справка.
7) exit - выход.
"""
    )


def input_book_data() -> Book:
    """Ввод параметров книги и создание объекта книги

    :return: Книга с введенными параметрами
    :rtype: Book

    :raises TitleTooLongException: Введено слишком длинное название
    :raises EmptyTextException: Введен пустой текст
    :raises InvalidYearException: Введено неверное значение года
    :raises InvalidStatusException: Введен неверный статус
    """

    title = input(">> Название: ")
    author = input(">> Автор: ")
    year = int(input(">> Год: "))
    status = input(">> Статус: ")

    return Book(title=title, author=author, year=year, status=status)


def find_book() -> Book | None:
    """Поиск книги с выбором режима поиска
    по ID, по названию, по автору или по году.

    :return: Найденная книга
    :rtype: Book or None

    :raises InvalidSearchModeException: Выбран неверный режим поиска
    """

    mode = input(
        """
>> Выберите режим поиска:  
    1. По ID
    2. По названию
    3. По автору
    4. По году                  
>> """
    )

    match mode:
        case "1":
            id = input(">> Введите ID: ")
            book = library.get(id=id)

        case "2":
            title = Title(input(">> Введите название: "))
            book = library.get(title=title)

        case "3":
            author = Author(input(">> Введите автора: "))
            book = library.filter(author=author)

            if book:
                book = book[0]

        case "4":
            year = Year(int(input(">> Введите год: ")))
            book = library.filter(year=year)

            if book:
                book = book[0]

        case _:
            raise InvalidSearchModeException

    return book
