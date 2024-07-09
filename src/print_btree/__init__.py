from src.print_btree.btree_to_list import btree_to_list
from src.print_btree.btree_list_printer import display

def print_btree(
    root, none_val='?'
) -> None:
    """
    Args:
        root: root of binary tree

        none_val: value to print if value is None
    """
    if none_val == ' ':
        raise Exception('none value cannot be whitespace')
    ls = btree_to_list(root)
    display(ls, none_val=none_val)

__all__ = ['print_btree']