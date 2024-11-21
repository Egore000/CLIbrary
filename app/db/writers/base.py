from abc import ABC, abstractmethod
from typing import TypeVar


Data = TypeVar("Data", bound=dict)


class BaseWriter(ABC):

    @abstractmethod
    def write(self, data: Data):
        ...
