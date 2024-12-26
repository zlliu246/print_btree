
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

        # used later
        self.wideness_score: int = 0

    def __str__(self):
        return f"Node(val={self.val}, wideness_score={self.wideness_score})"
    
    def __repr__(self):
        return self.__str__()
