from dataclasses import dataclass


@dataclass
class Color:
    black: str = "\033[30m"
    red: str = "\033[31m"
    green: str = "\033[32m"
    yellow: str = "\033[33m"
    blue: str = "\033[34m"
    purple: str = "\033[35m"
    white: str = "\033[37m"

    reset: str = "\033[0m"

    