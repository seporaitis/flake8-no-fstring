import ast
import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version


class NoFstringChecker(object):
    """
    A flake8 plugin to ban f-strings.
    """

    name = "flake8-no-fstring"
    version = version("flake8-no-fstring")

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree

    message_NF001 = "NF001 No f-strings."

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.JoinedStr):
                yield (node.lineno, node.col_offset, self.message_NF001, type(self))
