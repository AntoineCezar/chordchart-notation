import typing

from ..errors import ParseError
from ..text import Text
from ..ast import TerminalNode
from ..results import Results

from .parser import Parser

ResultsORTerminalNode = typing.Union[Results, TerminalNode]


class String(Parser):

    def __init__(self, string: str) -> None:
        self._string = string

    def __eq__(self, other):
        return isinstance(other, String) \
           and other._string == self._string

    def __add__(self, other: 'Parser') -> 'Parser':
        if isinstance(other, String):
            return String(self._string + other._string)

        return super().__add__(other)

    def parse(self, text: Text, results: ResultsORTerminalNode) -> None:
        lookup_length = len(self._string)
        fragment = text.lookup(lookup_length)

        if fragment == self._string:
            text.forward(lookup_length)
            results.append(fragment)
            return

        raise ParseError(f'"{self._string}"', text.position)
