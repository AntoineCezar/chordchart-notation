import unittest

from chordchart_notation.parser.ast.terminal_node import TerminalNode
from chordchart_notation.parser.parsers.create_node import CreateNode
from chordchart_notation.parser.parsers.string import String
from chordchart_notation.parser.text import Text


class TestParse(unittest.TestCase):

    def test_it_appends_created_node_to_results_when_successful(self):
        name = 'node name'
        parser = CreateNode(String('abc'), name)
        results = []

        parser.parse(Text('abc123'), results)

        self.assertListEqual(results, [TerminalNode(name, 'abc')])
