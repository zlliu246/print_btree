from typing import Any
from textwrap import dedent

from .helpers.tree_helper import (
    cast_to_standard_node,
    assign_wideness_scores,
    get_node_levels,
)
from .helpers.string_helper import (
    get_underscore_line_for_root_node,
    get_pipe_line,
    get_underscore_line,
    remove_unnecessary_underscores,
)
from .helpers.classes import Node

def print_btree(
    node: Any,
    val: str = "val",
    left: str = "left",
    right: str = "right",
    print_only: bool = True,
) -> str:
    """
    Args:
        node (Any): your own node object
        val (str): name of value in your node object. defaults to "val"
        left (str): name of left child in your node object. defaults to "left"
        right (str): name of right child in your node object. defaults to "right"
        print_only (bool): if true, print the binary tree representation and don't return. Else, don't print, but return 
    """
    
    node: Node = cast_to_standard_node(node, val, left, right)

    assign_wideness_scores(node)

    node_levels: list[list[Node]] = get_node_levels(node)

    # initialize lines to print
    lines_to_print: list[str] = []
    lines_to_print.append(get_underscore_line_for_root_node(node))

    for parent_node_level in node_levels:        
        # get pipe line
        pipe_line: str = get_pipe_line(lines_to_print[-1])
        lines_to_print.append(pipe_line)

        # get underscore line
        underscore_line: str = get_underscore_line(parent_node_level, pipe_line)
        lines_to_print.append(underscore_line)

    lines_to_print: list[str] = remove_unnecessary_underscores(lines_to_print)

    str_to_print = dedent("\n".join(lines_to_print))

    if print_only:
        print(str_to_print)
    else:
        return str_to_print


__all__ = ['print_btree']