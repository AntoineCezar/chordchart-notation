import abc

from ..text import Text
from ..results import Results


class Parser(abc.ABC):

    @abc.abstractmethod
    def parse(self, text: Text, results: Results) -> None:
        pass

    @abc.abstractmethod
    def __eq__(self, other):
        pass

    def __add__(self, other: 'Parser') -> 'Parser':
        from .add import Add

        return Add(self, other)

    def __or__(self, other: 'Parser') -> 'Parser':
        from .or_ import Or

        return Or(self, other)

    def __invert__(self):
        from .not_ import Not

        return Not(self)

    def __getitem__(self, key):
        from .many import Many
        from .maybe import Maybe

        if key == '?':
            return Maybe(self)

        if key == '+':
            return Many(self)

        if key == '*':
            return Maybe(Many(self))

        raise ValueError(key)

    def skip(self):
        from .skip import Skip

        return Skip(self)

    def node(self, name: str) -> 'Parser':
        from .create_node import CreateNode

        return CreateNode(self, name)
