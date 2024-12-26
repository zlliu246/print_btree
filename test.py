from src.print_btree import print_btree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node('apple')
root.left = Node('pie')
root.right = Node('juice')
root.left.left = Node('pear')
root.left.right = Node('pineapplejuice')
root.right.right = Node('durian')

print_btree(root)