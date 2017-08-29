import typing

from .node import Node


class RootNode(Node):
    _name = '__root__'

    def __init__(self, *nodes: Node) -> None:
        self._nodes = list(nodes)

    def __repr__(self):
        return str(self.sexpression())

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, RootNode) \
           and self._nodes == other._nodes

    def __contains__(self, item):
        return item in self._nodes

    def append(self, node: Node) -> None:
        self._nodes.append(node)

    def sexpression(self):
        return (
            self._name,
            *tuple(node.sexpression() for node in self._nodes)
        )

    def accept(self, visitor):
        for node in self._nodes:
            visitor.visit(node)
