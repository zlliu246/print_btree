from collections import deque

def get_height(root):
    """
    given root of btree, find height of tree
    """
    largest = -1
    queue = deque([(root, 1)])
    while queue:
        current, lvl = queue.popleft()
        if lvl > largest:
            largest = lvl
        if current.left: queue.append((current.left, lvl+1))
        if current.right: queue.append((current.right, lvl+1))
    return largest

def btree_to_list(root) -> list[list]:
    """
    generates 2d list representing btree
        eg. [[1], [2,3], [4,5,6,7]]
    """
    height = get_height(root)
    out = [[] for i in range(height)]
    queue = deque([(root, 0)])
    while queue:
        current, lvl = queue.popleft()
        if lvl > height-1:
            continue
        
        if current is None:
            out[lvl].append(None)
            queue.append((None, lvl+1))
            queue.append((None, lvl+1))
        else:
            out[lvl].append(current.val)
            queue.append((current.left, lvl+1))
            queue.append((current.right, lvl+1))
    return out