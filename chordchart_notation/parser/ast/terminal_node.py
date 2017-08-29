import typing

from .node import Node


MaybeString = typing.Union[None, typing.AnyStr]


class TerminalNode(Node):

    def __init__(self, name: str, value: MaybeString=None) -> None:
        self._name = name
        self._value = '' if value is None else value

    def __repr__(self):
        return str(self.sexpression())

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, TerminalNode) \
           and other._name == self._name \
           and other._value == self._value

    def append(self, fragment: str) -> None:
        self._value = self._value + fragment

    def sexpression(self) -> tuple:
        return (self._name, self._value)

    @property
    def value(self):
        return self._value
