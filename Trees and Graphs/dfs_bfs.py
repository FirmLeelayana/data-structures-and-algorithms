# Implementation of depth first search and breath first search.

from collections import deque
from graph import Node
from graph import Graph

def depth_first_search(node, value):
    if node.data == value:
        return node
    node.visited = True
    for n in node.adjacent_nodes:
        if not n.visited:
            return depth_first_search(n, value)

def breath_first_search(node, value):
    queue = deque()
    queue.append(node)

    while len(queue) > 0:
        current_node = queue.popleft()
        current_node.visited = True
        if current_node.data == value:
            return current_node
        else:
            for n in current_node.adjacent_nodes:
                if not n.visited:
                    queue.append(n)

if __name__ == "__main__":
    node = Node(3)
    node2 = Node(5)
    node3 = Node(6)
    node4 = Node(7)

    node.adjacent_nodes = [node2, node3]
    node2.adjacent_nodes = [node4]

    print(breath_first_search(node, 7))
