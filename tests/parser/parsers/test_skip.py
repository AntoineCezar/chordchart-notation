import unittest

from chordchart_notation.parser.errors import ParseError
from chordchart_notation.parser.parsers.skip import Skip
from chordchart_notation.parser.parsers.string import String
from chordchart_notation.parser.text import Text


class TestParse(unittest.TestCase):

    def test_it_does_not_modify_resuls_when_successful(self):
        parser = Skip(String('a'))
        results = []

        try:
            parser.parse(Text('aaa'), results)
        except ParseError:
            self.assertListEqual(results, [])
