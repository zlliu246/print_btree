import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(sys.path[0]).parent))

from print_btree import (
    StandardNode, cast, listify, gen_rows, drop_none, shorten, print_btree
)

class PrintBtreeTestCase(unittest.TestCase):

    def test_cast(self):
        class SomeNode:
            def __init__(self, value):
                self.value = value
                self.left_node = None
                self.right_node = None

        root = SomeNode(1)
        root.left_node = SomeNode(2)
        root.right_node = SomeNode(3)
        root.right_node.left_node = SomeNode(4)
        newroot = cast(
            root, val="value", left="left_node", right="right_node"
        )
        assert isinstance(newroot, StandardNode)
        assert newroot.val == 1
        assert newroot.left.val == 2
        assert newroot.right.val == 3
        assert newroot.right.left.val == 4
        
    def test_listify(self):
        root = StandardNode(1)
        root.left = StandardNode(2)
        root.right = StandardNode(3)
        root.left.left = StandardNode(4)
        root.right.left = StandardNode(6)
        ls = listify(root)
        assert ls == [['4', None, '6', None], ['2', '3'], ['1']]

    def test_gen_rows(self):
        ls = [['4', None, '6', None], ['2', '3'], ['1']]
        rows = gen_rows(ls)
        assert rows == [
            '4    ?    6    ?', 
            '|    |    |    |', 
            '__2___    __3___', 
            '  |         |   ', 
            '  _____1_____   '
        ]

    def test_drop_none(self):
        rows = [
            '4    ?    6    ?', 
            '|    |    |    |', 
            '__2___    __3___', 
            '  |         |   ', 
            '  _____1_____   '
        ]
        newrows = drop_none(rows)
        assert newrows == [
            '  _____1_____   ', 
            '  |         |   ', 
            '__2       __3   ', 
            '|         |     ', 
            '4         6     '
        ]

    def test_shorten(self):
        rows = [
            "    _____________1____________   ",
            "    |                        |   ",
            "    2                        3   "
        ]
        newrows = shorten(rows)
        assert newrows == [
            ' ___1___ ', 
            ' |     | ', 
            ' 2     3 '
        ]

if __name__ == "__main__":
    unittest.main()