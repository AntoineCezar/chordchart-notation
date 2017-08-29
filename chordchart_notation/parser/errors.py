from .position import Position


def escape(string):
    return string.replace('\n', '\\n') \
                 .replace('\r', '\\r') \
                 .replace('\t', '\\t')


class ParseError(Exception):
    """ Used when the parsing fails. """

    def __init__(self, expected: str, position: Position) -> None:
        Exception.__init__(self, f'expected: {escape(expected)} at {position}')
        self.expected = expected
        self.position = position
