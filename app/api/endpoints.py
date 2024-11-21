from tools.inputters.books import StatusInputter
from tools.services import input_book_data, library 


def add_book():
    book = input_book_data()
    library.add(book)
    print(f"Книга добавлена: ID = {book.id}")


def get_book():
    id = input(">> Введите ID: ")
    book = library.get(id=id)
    print(book.as_dict())


def get_all_books():
    print(library.get_all())
    

def delete_book():
    id = input(">> Введите ID: ")
    library.delete(id)


def change_status():
    id = input(">> ID: ")
    status = StatusInputter.input()
    library.change_status(id=id, status=status)
    

def help():
    pass

