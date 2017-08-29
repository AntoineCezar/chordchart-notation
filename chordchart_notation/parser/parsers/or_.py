from ..errors import ParseError
from ..text import Text

from .parser import Parser


class Or(Parser):

    def __init__(self, *parsers: Parser) -> None:
        self._parsers = parsers

    def __eq__(self, other):
        return isinstance(other, Or) \
           and other._parsers == self._parsers

    def __or__(self, other: Parser) -> 'Or':
        if isinstance(other, Or):
            parsers = self._parsers + other._parsers
            return Or(*parsers)

        return Or(self, other)

    def parse(self, text: Text, results) -> None:
        mark = text.mark()
        errors = []

        for parser in self._parsers:
            try:
                parser.parse(text, results)
                return
            except ParseError as e:
                text.backtrack(mark)
                errors.append(e)

        expected = ' or '.join([e.expected for e in errors])
        raise ParseError(expected, text.position)
