from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self) -> str:
        val = self.val
        left = right = None
        if self.left: left = left.val
        if self.right: right = right.val
        return f'Node({val=}, {left=}, {right=})'

class BTree:
    @staticmethod
    def gen_btree(ls: list) -> Node:
        """
        ls: a list of values eg. [1,2,3,4,5,6,7]

        output: root of a binary tree, with values inserted in order
        """
        root = Node(ls[0])
        for i in range(1, len(ls)):
            BTree.add_one(root, ls[i])
        return root

    @staticmethod
    def add_one(node: Node, val) -> None:
        """
        add new val to node at next available spot
        """
        queue = deque([node])
        while queue:
            current = queue.popleft()

            if current.left is None: 
                current.left = Node(val)
                return
            if current.right is None:
                current.right = Node(val)
                return
            
            queue.append(current.left)
            queue.append(current.right)


if __name__ == '__main__':
    root = BTree.gen_btree([1,2,3,4,5,6,7])

    print(root.left.left)

