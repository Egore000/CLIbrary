from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar

Data = TypeVar("Data", bound=dict)


@dataclass
class BaseWriter(ABC):
    """Менеджер для записи данных в хранилище"""

    @abstractmethod
    def write(self, data: Data): ...
