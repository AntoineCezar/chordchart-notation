import typing

from ..errors import ParseError
from ..text import Text

from .parser import Parser


class Maybe(Parser):

    def __init__(self, parser: Parser) -> None:
        self._parser = parser

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, Maybe) \
           and other._parser == self._parser

    def parse(self, text: Text, results) -> None:
        try:
            self._parser.parse(text, results)
        except ParseError:
            pass
