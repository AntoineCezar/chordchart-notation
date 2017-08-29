from ..results import Results

from .internal_node import InternalNode
from .node import Node
from .terminal_node import TerminalNode


class NodeFactory(Results):

    def __init__(self, name: str) -> None:
        self._name = name

    def append(self, result):
        self.success(result)

    def success(self, result):
        if not hasattr(self, '_node'):
            if isinstance(result, str):
                self._node = TerminalNode(self._name)
            elif isinstance(result, Node):
                self._node = InternalNode(self._name)
            else:
                raise ValueError(result)

        self._node.append(result)

    @property
    def node(self):
        return self._node
