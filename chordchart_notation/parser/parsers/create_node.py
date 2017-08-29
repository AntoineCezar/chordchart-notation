import typing

from ..ast.node_factory import NodeFactory
from ..results import Results
from ..text import Text

from .parser import Parser


class CreateNode(Parser):

    def __init__(self, parser: Parser, name: str) -> None:
        self._parser = parser
        self._name = name

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, CreateNode) \
           and other._parser == self._parser \
           and other._name == self._name

    def parse(self, text: Text, results: Results) -> None:
        node_factory = NodeFactory(self._name)

        self._parser.parse(text, node_factory)

        results.append(node_factory.node)
