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
    display: bool = True,
) -> str:
    
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

    if display:
        print(str_to_print)
    return str_to_print


__all__ = ['print_btree']