import typing

from ..results import Results
from ..text import Text
from ..results import SkipedResults

from .parser import Parser


class Skip(Parser):

    def __init__(self, parser: Parser) -> None:
        self._parser = parser

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, Skip) \
           and other._parser == self._parser

    def parse(self, text: Text, results: Results) -> None:
        self._parser.parse(text, SkipedResults())
