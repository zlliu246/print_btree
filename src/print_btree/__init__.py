from .btree_to_list import btree_to_list
from .btree_list_printer import display_btree
from .btree_caster import cast
from .btree_audit import audit

def print_btree(
    root,
    val='val',
    left='left',
    right='right'
) -> None:
    """
    Args:
        root: root of binary tree

        val: name of .val variable in Node
        left: name of .left variable in Node
        right: name of .right variable in Node

            eg, if your Node's class definition is something like:

            class BNode:
                def __init__(self, v):
                    self.v = v
                    self.l = None
                    self.r = None

            use print_btree(root, val='v', left='l', right='r')

    """
    root = cast(root, val=val, left=left, right=right)
    ls = btree_to_list(root)
    rows = display_btree(ls)
    rows = audit(rows)

    print();[print(row) for row in rows[::-1]];print()

__all__ = ['print_btree']