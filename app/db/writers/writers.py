import json
from pathlib import Path
from typing import TypeVar

from config import JSON_FILE
from db.writers.base import BaseWriter


Data = TypeVar("Data", bound=dict)


class JSONWriter(BaseWriter):
    def write(
            self, 
            data: Data, 
            path: Path = JSON_FILE
        ):
        with open(path, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            