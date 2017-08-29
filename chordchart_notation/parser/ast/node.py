import abc


class Node(abc.ABC):

    @property
    def name(self):
        return self._name

    @abc.abstractmethod
    def sexpression(self) -> tuple:
        pass
