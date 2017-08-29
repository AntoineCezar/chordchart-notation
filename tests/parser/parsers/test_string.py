import unittest

from chordchart_notation.parser.errors import ParseError
from chordchart_notation.parser.parsers.add import Add
from chordchart_notation.parser.parsers.parser import Parser
from chordchart_notation.parser.parsers.string import String
from chordchart_notation.parser.text import Text


class ParserMock(Parser):

    def parse(self, text: Text, results) -> None:
        pass

    def __eq__(self, other) -> bool:
        return other is self


class TestStringParse(unittest.TestCase):

    def test_it_appends_result_to_results_when_success(self):
        results = []

        String('abc').parse(Text('abc123'), results)

        self.assertListEqual(results, ['abc'])

    def test_it_raises_parse_error_when_fails(self):

        with self.assertRaises(ParseError):
            String('123').parse(Text('abc123'), [])


class TestAdd(unittest.TestCase):

    def test_it_extends_matched_string_when_same_type(self):
        parser = String('abc') + String('123')
        results = []

        parser.parse(Text('abc123'), results)

        self.assertListEqual(results, ['abc123'])

    def test_it_returns_add_parser_when_not_same_type(self):
        parser_a = String('abc')
        parser_b = ParserMock()

        parser = parser_a + parser_b

        self.assertEqual(parser, Add(parser_a, parser_b))
