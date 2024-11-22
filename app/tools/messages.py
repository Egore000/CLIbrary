from dataclasses import dataclass

from tools.colors import Color


@dataclass
class Message:
    """Сообщения в терминале
    
    Добавление цвета - исключительно в качестве эксперимента =)
    """

    greeting: str = f"""
            <<<     {Color.red}CLI{Color.reset}brary    >>>
    
Чтобы начать работу, ознакомься со списком команд:
1) {Color.green}get{Color.reset} - найти нужную книгу по названию, автору или году.
2) {Color.green}all{Color.reset} - вывести все имеющиeся книги.
3) {Color.green}add{Color.reset} - добавить книгу.
4) {Color.green}delete{Color.reset} - удалить книгу.
5) {Color.green}status{Color.reset} - изменить статус книги.
6) {Color.yellow}help{Color.reset} - справка.
7) {Color.red}exit{Color.reset} - выход.
"""

    id: str = f">> {Color.green}ID{Color.reset}: "
    title: str = f">> {Color.green}Название{Color.reset}: "
    author: str = f">> {Color.green}Автор{Color.reset}: "
    year: str = f">> {Color.green}Год{Color.reset}: "
    status: str = f">> {Color.green}Статус{Color.reset}: "

    help: str = f"""
1) {Color.green}get{Color.reset} - найти нужную книгу по названию, автору или году.
2) {Color.green}all{Color.reset} - вывести все имеющиeся книги.
3) {Color.green}add{Color.reset} - добавить книгу.
4) {Color.green}delete{Color.reset} - удалить книгу.
5) {Color.green}status{Color.reset} - изменить статус книги.
6) {Color.yellow}help{Color.reset} - справка.
7) {Color.red}exit{Color.reset} - выход.
"""
    mode: str =  f"""
>> Выберите режим поиска:  
    1. По {Color.green}ID{Color.reset}
    2. По {Color.green}названию{Color.reset}
    3. По {Color.green}автору{Color.reset}
    4. По {Color.green}году{Color.reset}                  
>> """
    
    added: str = f"Книга добавлена: {Color.green}ID{Color.reset} = "
    deleted: str = f"Книга успешно {Color.blue}удалена{Color.reset}"

    error: str = f"{Color.red}Произошла ошибка:{Color.reset}"
    input: str = f"{Color.blue}>> {Color.reset}"
