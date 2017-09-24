from .or_ import Or
from .parser import Parser
from .string import String


def AnyOf(*strings: str) -> Or:
    parsers = [String(string) for string in strings]
    return Or(*parsers)
