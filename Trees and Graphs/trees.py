# Implementation of a binary tree class.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


class Tree:
    def __init__(self, root=None):
        self.root = root