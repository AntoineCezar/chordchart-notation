import unittest
from chordchart_notation.parser.text import Text
from chordchart_notation.parser.position import Position


class TestTextLookup(unittest.TestCase):

    def test_it_returns_chars_when_chars_left(self):
        text = Text('abc123')

        fragment = text.lookup(3)

        self.assertEqual(fragment, 'abc')


class TestTextForward(unittest.TestCase):

    def test_it_forward_text_from_given_length(self):
        text = Text('abc123')

        text.forward(3)

        self.assertEqual(text.lookup(3), '123')


class TestTextPosition(unittest.TestCase):

    def test_it_starts_at_line_1_column_1(self):
        text = Text('abc\n123')

        self.assertEqual(text.position, Position(1, 1))

    def test_it_increment_line_on_each_newline(self):
        text = Text('abc\n123\nxyz\n789\n')
        text.forward(16)

        self.assertEqual(text.position.line, 5)

    def test_it_increment_column_when_not_newline(self):
        text = Text('abc\n123')
        text.forward(3)

        self.assertEqual(text.position.column, 4)

    def test_it_reset_column_on_newline(self):
        text = Text('abc\n123')
        text.forward(4)

        self.assertEqual(text.position.column, 1)


class TestBacktrack(unittest.TestCase):

    def test_it_restores_mark_s_position(self):
        text = Text('abc123')
        fragment = text.lookup(3)

        mark = text.mark()
        text.forward(3)
        text.backtrack(mark)

        self.assertEqual(fragment, text.lookup(3))
