import typing

from ..errors import ParseError
from ..results import Results
from ..text import Text

from .parser import Parser


class Many(Parser):

    def __init__(self, parser: Parser) -> None:
        self._parser = parser

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, Many) \
           and other._parser == self._parser

    def __invert__(self):
        return Many(~self._parser)

    def parse(self, text: Text, results: Results) -> None:
        has_at_least_one_sucess = False

        while True:
            try:
                self._parser.parse(text, results)
                has_at_least_one_sucess = True
            except ParseError as e:
                if not has_at_least_one_sucess:
                    raise e

                return
