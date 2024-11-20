from dataclasses import dataclass


@dataclass(eq=False)
class ApplicationException(Exception):
    """Базовое исключение для приложения"""

    @property
    def message(self):
        return "Что-то пошло не так..."
