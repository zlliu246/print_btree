from src.print_btree import print_btree

class Node:
    def __init__(self, value):
        self.value = value
        self.l = self.r = None

root = Node(1)
root.l = Node('apple')
root.r = Node('orange')
root.l.l = Node(3)
root.l.r = Node(4)
root.r.r = Node('pineapple')
root.r.r.l = Node(1000000)

print_btree(root, val='value', left='l', right='r')