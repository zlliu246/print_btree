import re
from collections import deque

class StandardNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class BtreeSpaceException(Exception):
    pass

def cast(oldroot, val='val', left='left', right='right'):
    """convert all nodes to StandardNode objects"""
    newroot = StandardNode(getattr(oldroot, val))
    if getattr(oldroot, left):
        left_child = cast(getattr(oldroot, left), val=val, left=left, right=right)
        newroot.left = left_child
    if getattr(oldroot, right):
        right_child = cast(getattr(oldroot, right), val=val, left=left, right=right)
        newroot.right = right_child
    return newroot

def listify(root: StandardNode):
    """root -> [[1], [2,3], [4,5,6,7]]"""
    def get_height(node: StandardNode):
        """find height of btree"""
        if node.left is None and node.right is None: return 1
        left_height = get_height(node.left) if node.left else 0
        right_height = get_height(node.right) if node.right else 0
        return 1 + max(left_height, right_height)

    height = get_height(root)
    pq = deque([(root, 0)])
    out = []
    while pq:
        current, lvl = pq.popleft()
        if lvl+1 > height: continue
        if lvl+1 > len(out): out.append([])
        out[lvl].append(str(current.val).replace(' ', '') if current else None)
        pq.append((current.left if (current and current.left) else None, lvl+1))
        pq.append((current.right if (current and current.right) else None, lvl+1))
    return out[::-1]

def gen_rows(rows: list[str], num_spaces=4) -> list[str]:
    """[[1], [2,3], [4,5,6,7]] to:
    
      _____1_____   
      |         |   
    __2___    __3___
    |    |    |    |
    4    5    6    7

    """
    def get_pipe_row(value_row: str) -> str:
        """returns line containing | characters """
        def transform(match: re.Match) -> str:
            return '|'.center(len(match.group()))
        return re.sub('[^ ]+', transform, value_row)
    
    def get_value_row(pipe_row: str, values: list[str|None]):
        """returns line containing the values (no | characters) """
        itr = iter(values)
        def transform(match: re.Match, itr=itr) -> str:
            word = next(itr)
            return (str(word) if word else '?').center(len(match.group()), '_')
        return re.sub(r'\| +\|', transform, pipe_row)
    
    top = (' '*num_spaces).join([(v if v else '?') for v in rows[0]])
    out = [top]
    for row in rows[1:]:
        pipe_row = get_pipe_row(out[-1])
        value_row = get_value_row(pipe_row, row)
        for v in value_row.split():
            if v and (v[:2]!='__' and v[-2:]!='__'):
                return gen_rows(rows, num_spaces=num_spaces*2)
        out.extend([pipe_row, value_row])
    return out

def drop_none(rows: list[str]) -> list[str]:
    """
      _____1_____   
      |         |   
    __2___    __3___
    |    |    |    |
    4    ?    6    ?

    to:

      _____1_____   
      |         |   
    __2       __3
    |         |    
    4         6    
 
    """
    def f_pipe_row(row: str, prev: str) -> str:
        out = ''
        for i,char in enumerate(row):
            if char != '|': out += char
            else: 
                if i<len(prev) and prev[i] != ' ': out += '|'
                else: out += ' '
        return out
    def f_value_row(row: str, prev: str) -> str:
        def transform(match: re.Match, prev=prev) -> str:
            start, end = match.span()
            s = prev[start:end]
            if len(set(s))==1 and s[0]==' ': return ' ' * len(match.group())
            else: return '_' * len(match.group())
        return re.sub('_+', transform, row.replace('?', ' '))
    top = rows[0].replace('?', ' ')
    out = [top]
    is_pipe = True
    for row in rows[1:]:
        if is_pipe: out.append(f_pipe_row(row, out[-1]))
        else: out.append(f_value_row(row, out[-1]))
        is_pipe = not is_pipe
    return out[::-1]

def shorten(rows: list[str]) -> list[str]:
    """
    
    _____________1____________
    |                        |
    2                        3
    
    to:

    __1__
    |   |
    2   3

    """
    def normalize(rows: list[str]) -> list[str]:
        maxlen = len(max(rows, key=len))
        for i in range(len(rows)): 
            rows[i] = ' ' + rows[i].ljust(maxlen) + ' '
        return rows
    def transpose(rows: list[str]) -> list[str]:
        out = []
        for i in range(len(rows[0])):
            row = ''
            for j in range(len(rows)):
                row += rows[j][i]
            out.append(row)
        return out
        
    rows = transpose(normalize(rows))
    
    out = []
    for i in range(1, len(rows)-1):
        chars = set(rows[i-1] + rows[i] + rows[i+1])
        if chars != {' ', '_'} and chars != {' '}: 
            out.append(rows[i])
    
    return transpose(out)

def print_btree(root, val='val', left='left', right='right'):
    """
    Prints a binary tree in human readable format

    Args:
        root (Node): root of a binary tree
        val (str): string name of node's value
        left (str): string name of node's left child
        right (str): string name of node's right child

        class Node:
            def __init__(self, val):
                self.val = val
                self.left = None
                self.rght = None

        ^ for this Node class, 
            val='val', left='left', right='right'

        class MyNode:
            def __init__(self, n):
                self.value = n
                self.left_child = None
                self.right_child = None

        ^ for this MyNode class,
            val='value', left='left_child', right='right_child'
    
    """
    root = cast(root, val=val, left=left, right=right)
    ls = listify(root)
    rows = gen_rows(ls)
    rows = drop_none(rows)
    rows = shorten(rows)
    for row in rows:
        print(row)
    print()

__all__ = ['print_btree']