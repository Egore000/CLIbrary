from dataclasses import dataclass

from tools.exceptions.commands import (EmptyCommandException,
                                       UnknownCommandException)


@dataclass
class Command:
    """Команда в терминале"""

    __allowed_commands = ["get", "all", "add", "delete", "status", "help", "exit"]
    value: str

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.value:
            raise EmptyCommandException()

        self.value = self.value.lower().strip()
        if self.value not in self.__allowed_commands:
            raise UnknownCommandException(self.value)
