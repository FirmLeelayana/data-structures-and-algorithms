# Given a linked list, delete a node within somewhere in the middle, where the only input is the node that is required to be deleted.
# Time complexity: O(1), space complexity: O(1)

from linked_list import Node
from linked_list import LinkedList

def delete_middle_node(node):
    """Given a node, delete this node within a linked list.
    
    Input: node, node object
    Output: -
    """

    node.data = node.next.data
    node.next = node.next.next

if __name__ == "__main__":
    llist = LinkedList(["a", "b", "c", "d"])
    node = llist.head.next.next
    delete_middle_node(node)
    print(llist)