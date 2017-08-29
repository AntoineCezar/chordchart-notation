import typing

from ..results import Results
from ..results import DeferredResults
from ..text import Text

from .parser import Parser


class Add(Parser):

    def __init__(self, *parsers: Parser) -> None:
        self._parsers = parsers

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, Add) \
           and other._parsers == self._parsers

    def __add__(self, other: Parser) -> 'Add':
        if isinstance(other, Add):
            parsers = self._parsers + other._parsers
            return Add(*parsers)

        return Add(self, other)

    def parse(self, text: Text, results: Results) -> None:
        results = DeferredResults(results)

        for parser in self._parsers:
            parser.parse(text, results)

        results.deliver()
