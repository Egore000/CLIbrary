from api.endpoints import (
    add_book,
    change_status,
    clear,
    delete_book,
    get_all_books,
    get_books,
    help,
)

router = {
    "get": get_books,
    "all": get_all_books,
    "add": add_book,
    "delete": delete_book,
    "status": change_status,
    "help": help,
    "clear": clear,
    "exit": exit,
}
