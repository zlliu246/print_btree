from src.print_btree.utils import BTree

def test_gen_btree():
    root = BTree.gen_btree([1, 2, 3])
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left is None
    assert root.right.right is None

def test_gen_btree_2():
    root = BTree.gen_btree([1,2,3,4,5,6,7,8])
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left.val == 4
    assert root.left.right.val == 5
    assert root.right.left.val == 6
    assert root.right.right.val == 7
    assert root.left.left.left.val == 8