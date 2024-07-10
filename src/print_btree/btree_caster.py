class StandardizedNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def cast(
    node, 
    val: str = 'val', 
    left: str = 'left', 
    right: str = 'right'
) -> StandardizedNode:
    """
    takes in node, creates copy of binary tree
        where all nodes in copy are
        StandardizedNodes (.val, .left, .right)
    """
    if node is None:
        return None
    
    node_val = getattr(node, val)
    node_val = str(node_val).replace(' ', '-')
    s_node = StandardizedNode(node_val)

    s_node.left = cast(
        getattr(node, left), val=val, left=left, right=right
    )
    s_node.right = cast(
        getattr(node, right), val=val, left=left, right=right
    )
    return s_node

