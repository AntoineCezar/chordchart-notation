import unittest

from chordchart_notation.parser.errors import ParseError
from chordchart_notation.parser.parsers.many import Many
from chordchart_notation.parser.parsers.string import String
from chordchart_notation.parser.text import Text


class TestParse(unittest.TestCase):

    def test_it_raise_parse_error_when_not_a_single_match(self):
        parser = Many(String('a'))

        with self.assertRaises(ParseError):
            parser.parse(Text('bbb'), [])

    def test_it_parses_as_many_available_matches(self):
        parser = Many(String('a'))
        results = []

        parser.parse(Text('aaabbb'), results)

        self.assertEqual(results, ['a', 'a', 'a'])


class TestInvert(unittest.TestCase):

    def test_invert_returns_many_with_inverted_wrapped_parser(self):
        parser = String('a')

        self.assertEqual(~Many(parser), Many(~parser))
