# Эндпоинты для взаимодействия с приложением

from pprint import pprint

from domain.values.books import Status
from tools.services import find_book, input_book_data, library


def add_book():
    """Добавление книги"""
    book = input_book_data()
    library.add(book)
    print(f"Книга добавлена: ID = {book.id}")


def get_book():
    """Поиск книги по заданным параметрам"""
    book = find_book()
    try:
        pprint(book.as_dict(), indent=4, depth=2, sort_dicts=False)
    except (TypeError, AttributeError):
        pprint([item.as_dict() for item in book], indent=4, depth=2, sort_dicts=False)


def get_all_books():
    """Вывод всех книг, хранящихся в БД"""
    pprint(library.get_all(), indent=4, depth=2, sort_dicts=False)


def delete_book():
    """Удаление книги"""
    id = input(">> Введите ID: ")
    library.delete(id)


def change_status():
    """Изменение статуса книги"""
    id = input(">> ID: ")
    status = Status(input(">> Статус: "))
    library.change_status(id=id, status=status)


def help():
    """Помощь с работой приложения"""
    print(
        """
1) get - найти нужную книгу по названию, автору или году.
2) all - вывести все имеющиeся книги.
3) add - добавить книгу.
4) delete - удалить книгу.
5) status - изменить статус книги.
6) help - справка.
7) exit - выход.
"""
    )
