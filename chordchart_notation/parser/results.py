import abc
import typing

from .ast.node import Node


Result = typing.Union[str, Node]
ResultList = typing.List[Result]


class Results(abc.ABC):

    @abc.abstractmethod
    def append(self, result: Result) -> None:
        pass


class SkipedResults(Results):

    def append(self, result: Result):
        pass


class DeferredResults(Results):

    def __init__(self, recipient: Results) -> None:
        self._recipient = recipient
        self._results: ResultList = []

    def append(self, result: Result):
        self._results.append(result)

    def deliver(self):
        for result in self._results:
            self._recipient.append(result)


class UnexpectedResults(Results):

    def __init__(self) -> None:
        self._results: ResultList = []

    def append(self, result: Result):
        self._results.append(result)
