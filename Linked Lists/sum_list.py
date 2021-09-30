# Sum two linked lists together, where each linked list represents a number.
# Time complexity: O(n), space complexity: O(n)

from linked_list import Node
from linked_list import LinkedList

def sum_list_recursive(node_one, node_two, carry):
    "Recursively calculates the nodes required in the new linked list."

    if (node_one is None) and (node_two is None) and (carry is 0):
        return None

    sum = carry

    if node_one is not None:
        sum += node_one.data
    
    if node_two is not None:
        sum += node_two.data

    new_node = Node(sum % 10)

    if sum >= 10:
        new_carry = 1
    else:
        new_carry = 0

    if (node_one is not None) and (node_two is not None):
        new_node.next = sum_list_recursive(node_one.next, node_two.next, new_carry)

    return new_node
    

def sum_list(llist_one, llist_two):
    "Takes in two linked lists and returns a sum of the two in the form of a new linked list."

    node_one = llist_one.head
    node_two = llist_two.head

    head_node = sum_list_recursive(node_one, node_two, 0)
    new_llist = LinkedList()
    new_llist.head = head_node

    return new_llist


if __name__ == "__main__":
    llist = LinkedList([1, 2, 3, 4])
    llist_two = LinkedList([1, 2, 3, 4])
    print(sum_list(llist, llist_two))

    llist = LinkedList([1, 2, 3, 4])
    llist_two = LinkedList([1, 2, 3])
    print(sum_list(llist, llist_two))

    llist = LinkedList([1, 2, 8, 4])
    llist_two = LinkedList([1, 2, 3])
    print(sum_list(llist, llist_two))