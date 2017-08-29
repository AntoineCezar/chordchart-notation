import unittest

from chordchart_notation.parser.errors import ParseError
from chordchart_notation.parser.parsers.add import Add
from chordchart_notation.parser.parsers.string import String
from chordchart_notation.parser.text import Text


class TestParse(unittest.TestCase):

    def test_it_chains_parsers(self):
        parser = Add(String('abc'), String('123'))
        results = []

        parser.parse(Text('abc123'), results)

        self.assertListEqual(results, ['abc', '123'])

    def test_it_does_not_modify_resuls_when_fails(self):
        parser = Add(String('a'), String('b'))
        results = []

        try:
            parser.parse(Text('ac'), results)
        except ParseError:
            self.assertListEqual(results, [])


class TestAdd(unittest.TestCase):

    def test_it_extends_parser_list_when_same_type(self):
        parser_a = String('abc')
        parser_b = String('123')

        parser = Add(parser_a) + Add(parser_b)

        self.assertEqual(parser, Add(parser_a, parser_b))

    def test_it_returns_add_parser_when_not_same_type(self):
        parser_a = Add()
        parser_b = String('abc')

        parser = parser_a + parser_b

        self.assertEqual(parser, Add(parser_a, parser_b))
