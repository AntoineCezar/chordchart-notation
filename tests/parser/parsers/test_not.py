import unittest

from chordchart_notation.parser.errors import ParseError
from chordchart_notation.parser.parsers.not_ import Not
from chordchart_notation.parser.parsers.string import String
from chordchart_notation.parser.text import Text
from chordchart_notation.parser.text import Position


class TestNotParse(unittest.TestCase):

    def test_it_raises_parse_error_when_parser_not_fails(self):
        parser = Not(String('abc'))

        with self.assertRaises(ParseError):
            parser.parse(Text('abc123'), [])

    def test_it_bactracks_when_parser_not_fails(self):
        text = Text('abc123')
        position = text.position
        parser = Not(String('abc'))

        try:
            parser.parse(text, [])
        except ParseError:
            pass

        self.assertEqual(text.position, position)

    def test_it_append_first_char_when_sucess(self):
        results = []

        Not(String('123')).parse(Text('abc123'), results)

        self.assertListEqual(results, ['a'])

    def test_it_forwards_text_by_one_char_when_sucess(self):
        string = 'abc123'
        text = Text(string)
        parser = Not(String('123'))

        parser.parse(text, [])

        expected = Text(string)
        expected.forward(1)
        self.assertEqual(text.position, expected.position)
