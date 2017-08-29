from .text import Text
from .ast import RootNode


def parse(grammar, string):
    text = Text(string)
    tree = RootNode()

    grammar.parse(text, tree)

    return tree
