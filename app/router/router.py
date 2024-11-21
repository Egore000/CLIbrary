from api.endpoints import add_book, get_book, get_all_books, \
    help, delete_book, change_status


router = {
    "get": get_book,
    "all": get_all_books,
    "add": add_book,
    "delete": delete_book,
    "status": change_status,
    "help": help,
    "exit": exit,
}