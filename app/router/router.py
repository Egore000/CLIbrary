from api.endpoints import (add_book, change_status, delete_book, get_all_books,
                           get_book, help)

router = {
    "get": get_book,
    "all": get_all_books,
    "add": add_book,
    "delete": delete_book,
    "status": change_status,
    "help": help,
    "exit": exit,
}
