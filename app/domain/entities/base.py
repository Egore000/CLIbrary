from __future__ import annotations

from abc import ABC
from dataclasses import dataclass


@dataclass
class Entity(ABC):
    """Базовая сущность"""

    def as_dict(self) -> dict:
        result = {}
        for key, value in self.__dict__.items():
            if hasattr(value, "as_generic_type"):
                result[key] = value.as_generic_type()
            else:
                result[key] = value
        return result

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, value: Entity) -> bool:
        return self.id == value.id
