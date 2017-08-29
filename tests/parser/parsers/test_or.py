import unittest

from chordchart_notation.parser.errors import ParseError
from chordchart_notation.parser.parsers.or_ import Or
from chordchart_notation.parser.parsers.add import Add
from chordchart_notation.parser.parsers.string import String
from chordchart_notation.parser.text import Text


class TestParse(unittest.TestCase):

    def test_it_stops_at_first_successful_parser(self):
        parser = Or(String('abc'), String('123'))
        results = []

        parser.parse(Text('abc123'), results)

        self.assertListEqual(results, ['abc'])

    def test_it_raises_parse_error_when_no_successful_parser(self):
        parser = Or(String('a'), String('b'))

        with self.assertRaises(ParseError):
            parser.parse(Text('123'), [])

    def test_it_merges_expectations_when_no_successful_parser(self):
        parser = Or(String('a'), String('b'))

        try:
            parser.parse(Text('123'), [])
        except ParseError as e:
            self.assertEqual(e.expected, '"a" or "b"')

    def test_it_provides_the_same_text_to_each_parser(self):
        text = Text('123')

        result = []
        parser = Or(Add(String('12'), String('4')),
                    String('123'))
        parser.parse(text, result)

        self.assertEqual(result, ['123'])


class TestOr(unittest.TestCase):

    def test_it_extends_parser_list_when_same_type(self):
        parser_a = String('abc')
        parser_b = String('123')

        parser = Or(parser_a) | Or(parser_b)

        self.assertEqual(parser, Or(parser_a, parser_b))

    def test_it_returns_add_parser_when_not_same_type(self):
        parser_a = Or()
        parser_b = String('abc')

        parser = parser_a | parser_b

        self.assertEqual(parser, Or(parser_a, parser_b))
