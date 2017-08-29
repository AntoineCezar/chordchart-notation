import typing

from ..results import Results
from ..text import Text

from .add import Add
from .many import Many
from .maybe import Maybe
from .parser import Parser


class SeparatedBy(Parser):

    def __init__(self, separator: Parser, element: Parser) -> None:
        self._separator = separator
        self._element = element

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, SeparatedBy) \
           and other._separator == self._separator \
           and other._element == self._element

    def parse(self, text: Text, results: Results) -> None:
        self._element.parse(text, results)

        repeats = Many(Add(self._separator, self._element))

        Maybe(repeats).parse(text, results)
