from dataclasses import dataclass
from enum import Enum

from tools.exceptions.commands import (EmptyCommandException,
                                       UnknownCommandException)


class AllowedCommands(Enum):
    """Разрешенные команды"""

    GET = "get"
    ALL = "all"
    ADD = "add"
    DELETE = "delete"
    STATUS = "status"
    HELP = "help"
    CLEAR = "clear"
    EXIT = "exit"


@dataclass
class Command:
    """Команда в терминале"""

    value: AllowedCommands

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.value:
            raise EmptyCommandException()

        self.value = self.value.lower().strip()
        if self.value not in AllowedCommands:
            raise UnknownCommandException(self.value)
