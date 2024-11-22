from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import TypeVar

Data = TypeVar("Data", bound=dict)


@dataclass
class BaseReader(ABC):
    """Менеджер для чтения данных из хранилища"""

    @abstractmethod
    def read(self, path: Path) -> Data: ...
