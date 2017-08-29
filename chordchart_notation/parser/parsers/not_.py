from ..errors import ParseError
from ..results import Results
from ..results import UnexpectedResults
from ..text import Text

from .parser import Parser


class Not(Parser):

    def __init__(self, parser: Parser) -> None:
        self._parser = parser

    def __eq__(self, other) -> bool:
        return isinstance(other, Not) \
           and other._parser == self._parser

    def parse(self, text: Text, results: Results) -> None:
        mark = text.mark()

        try:
            success_results = UnexpectedResults()
            self._parser.parse(text, success_results)
        except ParseError:
            fragment = text.lookup(1)
            text.forward(1)
            results.append(fragment)
            return

        text.backtrack(mark)
        raise ParseError(f'not "{success_results}"', text.position)
