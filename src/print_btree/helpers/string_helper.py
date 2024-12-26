"""
Contains helper functions for string manipulation operations
"""
import re

from .classes import Node

def get_underscore_str(node: Node) -> str:
    num_chars: int = node.wideness_score // 2
    spaces: str = " " * num_chars
    underscores: str = "_" * num_chars

    if node.left and node.right:
        return underscores + str(node.val) + underscores
    if node.left:
        return underscores + str(node.val) + spaces
    if node.right:
        return spaces + str(node.val) + underscores
    return str(node.val)

def get_underscore_line_for_root_node(node: Node) -> str:
    padding: str = " " * node.wideness_score
    return padding + get_underscore_str(node)

def get_underscore_line(
    parent_node_level: list[Node],
    previous_pipe_line: str
) -> str:
    chars = [" "] * len(previous_pipe_line) * 3
    prev_pipe_line_index: int = previous_pipe_line.find("|")

    for parent_node in parent_node_level:
        for child_node in [parent_node.left, parent_node.right]:
            if not child_node:
                continue
            # match child_node with pipe in previous_pipe_line
            child_underscore_str: str = get_underscore_str(child_node)
            left_index: int = prev_pipe_line_index - len(child_underscore_str)//2
            chars[left_index: left_index + len(child_underscore_str)] = list(child_underscore_str)

            prev_pipe_line_index: int = previous_pipe_line.find("|", prev_pipe_line_index + 1)

    return "".join(chars).rstrip()

def get_pipe_line(previous_underscore_line: str) -> str:
    chars: list[str] = [" "] * len(previous_underscore_line)
    for match in re.finditer(r"\b_|_\b", previous_underscore_line):
        index: int = match.span()[0]
        chars[index] = "|"
    return "".join(chars)

def remove_unnecessary_underscores(lines_to_print: list[str]) -> list[str]:
    indexes_to_remove: set[int] = set()

    max_index: int = max(len(line) for line in lines_to_print)

    for index in range(1, max_index):
        chars: set[str] = set()
        for line in lines_to_print:
            trio: str = line[index-1: index+2]
            chars.update(set(trio))
        if chars == {"_"} or chars == {" "} or chars == {"_", " "}:
            indexes_to_remove.add(index)

    line_lists_to_print: list[list[str]] = [list(line) for line in lines_to_print]
    for index in indexes_to_remove:
        for line_lists in line_lists_to_print:
            if index < len(line_lists):
                line_lists[index] = ""
    
    return ["".join(line_list) for line_list in line_lists_to_print]