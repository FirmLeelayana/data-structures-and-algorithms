# Implementation of graphs.

class Graph:
    
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def __repr__(self):
        return self.nodes

    def __iter__(self):
        for node in self.nodes:
            yield node


class Node:

    def __init__(self, data, adjacent_nodes=[]):
        self.data = data
        self.adjacent_nodes = adjacent_nodes
        self.visited = False

    def __repr__(self):
        return str(self.data)

    