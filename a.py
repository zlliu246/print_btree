from src.print_btree import print_btree
from src.print_btree.utils import BTree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)

root = BTree.gen_btree(['apple', 'orange', 'pear', 'pineapple', 'durian', 'appleorangepear'])

print_btree(root)