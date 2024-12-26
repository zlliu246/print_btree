from src.print_btree import print_btree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node("apple")
root.left = Node("orange")
root.right = Node("pear")
root.left.left = Node("pineapple")
root.left.right = Node("durian")
root.left.right.left = Node("durian tree apple orange pear")
root.left.right.left.right = Node("durian")
# root.right.left = Node("kiwi")
root.right.right = Node("avocado")

print_btree(root)