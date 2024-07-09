from src.print_btree.utils import BTree, Node
from src.print_btree.btree_to_list import get_height, btree_to_list

def test_get_height():
    root = BTree.gen_btree([1])
    assert get_height(root) == 1

    root = BTree.gen_btree([1,2])
    assert get_height(root) == 2

    root = BTree.gen_btree([1,2,3])
    assert get_height(root) == 2

    root = BTree.gen_btree([1,2,3,4])
    assert get_height(root) == 3

    root = BTree.gen_btree([1,2,3,4,5,6,7])
    assert get_height(root) == 3

    root = BTree.gen_btree([1,2,3,4,5,6,7,8])
    assert get_height(root) == 4

def test_btree_to_list():
    root = BTree.gen_btree([1,2,3,4,5,6,7])
    ls = btree_to_list(root)
    assert ls == [[1], [2,3], [4,5,6,7]]

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(5)
    root.right.left = Node(6)
    ls = btree_to_list(root)
    assert ls == [[1], [2,3], [5,None,6,None]]

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(5)
    root.right.left = Node(6)
    root.right.left.right = Node('apple')
    ls = btree_to_list(root)
    assert ls == [[1], [2,3], [5,None,6,None], [None, None, None, None, None, 'apple', None, None]]