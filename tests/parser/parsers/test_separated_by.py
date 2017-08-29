import unittest

from chordchart_notation.parser.parsers.separated_by import SeparatedBy
from chordchart_notation.parser.parsers.string import String
from chordchart_notation.parser.text import Text


class TestSeparatedBy(unittest.TestCase):

    def test_it_matches_subsequent_matches_prefixed_by_separator(self):
        parser = SeparatedBy(String(','), String('a'))
        results = []

        parser.parse(Text('a,a,a,'), results)

        self.assertEqual(results, ['a', ',', 'a', ',', 'a'])
