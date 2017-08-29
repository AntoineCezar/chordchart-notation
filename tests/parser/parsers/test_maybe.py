import unittest

from chordchart_notation.parser.errors import ParseError
from chordchart_notation.parser.parsers.maybe import Maybe
from chordchart_notation.parser.parsers.string import String
from chordchart_notation.parser.text import Text


class TestManyParse(unittest.TestCase):

    def test_it_does_not_raise_parse_error_when_fails(self):
        parser = Maybe(String('a'))

        try:
            parser.parse(Text('bbb'), [])
        except ParseError:
            self.fail('ParseError raised')
