import typing

from .node import Node


class InternalNode(Node):

    def __init__(self, name: str, *nodes: Node) -> None:
        self._name = name
        self._nodes = list(nodes)

    def __repr__(self):
        return str(self.sexpression())

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, InternalNode) \
           and self._nodes == other._nodes

    def append(self, node: Node) -> None:
        self._nodes.append(node)

    def sexpression(self) -> tuple:
        return (
            self._name,
            *tuple(node.sexpression() for node in self._nodes)
        )

    def accept(self, visitor):
        for node in self._nodes:
            visitor.visit(node)
