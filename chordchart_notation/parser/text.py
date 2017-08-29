import typing

from .position import Position


class Mark(typing.NamedTuple):
    index: int


class Text:

    def __init__(self, string: str) -> None:
        self._string = string
        self._index = 0

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, Text) \
           and other._string == self._string \
           and other._index == self._index

    def lookup(self, length: int) -> str:
        return self._string[self._index:self._index + length]

    def forward(self, length: int) -> None:
        self._index += length

    def mark(self) -> Mark:
        return Mark(self._index)

    def backtrack(self, mark: Mark) -> None:
        self._index = mark.index

    @property
    def position(self) -> Position:
        string = self._string[:self._index]
        line = string.count('\n') + 1
        last_line = string.split('\n')[-1]
        column = len(last_line) + 1

        return Position(
            line=line,
            column=column,
        )
