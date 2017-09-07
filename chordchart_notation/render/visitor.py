class Visitor:

    def visit(self, node):
        method = getattr(self, f'_visit_{node.name}', self._skip)
        method(node)

    def _skip(self, node):
        pass

    def _pass_thru(self, node):
        node.accept(self)
