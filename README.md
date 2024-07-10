# print-btree

This packages allows you to print and visualize your binary tree

```
from print_btree import print_btree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_btree(root)

'''

 __1__
 |   |
_2_  3 
| |    
4 5   

'''
```

Ideally, your Node definition should be something like:

```
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

But it's ok if your Node has different attribute names:

```
from print_btree import print_btree

class BNode:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

root = BNode(1)
root.left_node = BNode(2)
root.right_node = BNode(3)
root.left_node.left_node = BNode(4)
root.left_node.right_node = BNode(5)
root.right_node.right_node = BNode(100)

print_btree(root, 
            val='value',
            left='left_node',
            right='right_node')

'''

 __1__
 |   |
_2_  3__
| |    |
4 5   100

'''
```

It's ok if you values are longer

```
from print_btree import print_btree

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
'''
       ________apple________
       |                   |
 _____pie_____           juice_
 |           |                |
pear   pineapplejuice       durian

'''
```