class StandardizedNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def cast(node, val='val', left='left', right='right'):
    if node is None: return None
    node_val = getattr(node, val)
    node_val = str(node_val).replace(' ', '-')
    s_node = StandardizedNode(node_val)

    s_node.left = cast(getattr(node, left), val=val, left=left, right=right)
    s_node.right = cast(getattr(node, right), val=val, left=left, right=right)
    return s_node

