# Tree traversal methods.

from trees import Node
from trees import Tree

def in_order_traversal(node):
    node_order = []
    if node is not None:
        node_order.extend(in_order_traversal(node.left))
        node_order.append(node)
        node_order.extend(in_order_traversal(node.right))
    return node_order

def pre_order_traversal(node):
    node_order = []
    if node is not None:
        node_order.append(node)
        node_order.extend(pre_order_traversal(node.left))
        node_order.extend(pre_order_traversal(node.right))
    return node_order

def post_order_traversal(node):
    node_order = []
    if node is not None:
        node_order.extend(post_order_traversal(node.left))
        node_order.extend(post_order_traversal(node.right))
        node_order.append(node)
    return node_order
    
if __name__ == "__main__":
    node = Node(5)
    tree = Tree(node)
    second_node = Node(3)
    third_node = Node(7)
    fourth_node = Node(2)
    node.left = second_node
    node.right = third_node
    second_node.left = fourth_node

    print(in_order_traversal(node))
    print(pre_order_traversal(node))
    print(post_order_traversal(node))