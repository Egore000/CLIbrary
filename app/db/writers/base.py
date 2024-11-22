from abc import ABC, abstractmethod
from typing import TypeVar

Data = TypeVar("Data", bound=dict)


class BaseWriter(ABC):
    """Менеджер для записи данных в хранилище"""

    @abstractmethod
    def write(self, data: Data): ...
