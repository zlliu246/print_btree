"""
Contains helper functions for tree and traversal stuff
"""

from typing import Any, Deque
from collections import deque

from .classes import Node

def cast_to_standard_node(
    nonstandard_node: Any, 
    val: str = 'val', 
    left: str = 'left', 
    right: str = 'right'
) -> Node:
    """
    Converts nonstandard_node root to standard Node
    """
    standard_node = Node(getattr(nonstandard_node, val))

    if getattr(nonstandard_node, left):
        left_child = cast_to_standard_node(
            getattr(nonstandard_node, left), val=val, left=left, right=right
        )
        standard_node.left = left_child

    if getattr(nonstandard_node, right):
        right_child = cast_to_standard_node(
            getattr(nonstandard_node, right), val=val, left=left, right=right
        )
        standard_node.right = right_child

    return standard_node

def assign_wideness_scores(node: Node) -> None:
    """
    Recursively assigns wideness scores. Used in printing later on.
    """
    if not Node:
        return
    if node.left:
        assign_wideness_scores(node.left)
    if node.right:
        assign_wideness_scores(node.right)

    val_len: int = len(str(node.val))

    node.wideness_score = (
        val_len + 
        (node.left.wideness_score if node.left else 0) +
        (node.right.wideness_score if node.right else 0)
    )

def get_node_levels(node: Node) -> list[list[Node]]:
    
    node_levels: list[list[Node]] = []

    node_dq: Deque[tuple[Node, int]] = deque([(node, 0)])

    while node_dq:
        current_node, current_level = node_dq.popleft()

        if current_level > len(node_levels) - 1:
            node_levels.append([])
        
        node_levels[current_level].append(current_node)

        if current_node.left:
            node_dq.append((current_node.left, current_level + 1))
        if current_node.right:
            node_dq.append((current_node.right, current_level + 1))
        
    return node_levels
