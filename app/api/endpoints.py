# Эндпоинты для взаимодействия с приложением

from domain.values.books import Status
from repo.exceptions.books import ObjectNotFoundException
from tools.messages import Message
from tools.services import find_book, input_book_data, library


def add_book():
    """Добавление книги"""
    book = input_book_data()
    library.add(book)
    print(Message.added, book.id)


def get_book():
    """Поиск книги по заданным параметрам"""
    book = find_book()
    try:
        print(book.human_readable())
    except (TypeError, AttributeError):
        print([item.human_readable() for item in book])


def get_all_books():
    """Вывод всех книг, хранящихся в БД"""
    books = library.get_all()
    for book in books:
        print(book.human_readable())


def delete_book():
    """Удаление книги"""
    id = input(Message.id)
    library.delete(id)
    print(Message.deleted)


def change_status():
    """Изменение статуса книги"""
    id = input(Message.id)

    if library.exists(id):
        status = Status(input(Message.status))
        library.change_status(id=id, status=status)
    else:
        raise ObjectNotFoundException

def help():
    """Помощь с работой приложения"""
    print(Message.help)
