from enum import Enum


class Color(Enum):
    WHITE = '\033[37mW\033[0m'
    ORANGE = '\033[38;5;208mO\033[0m'
    GREEN = "\033[32mG\033[0m"
    RED = '\033[31mR\033[0m'
    BLUE = '\033[34mB\033[0m'
    YELLOW = '\033[33mY\033[0m'

