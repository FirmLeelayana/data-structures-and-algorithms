# Checks if linked list is a palindrome via recursion.
# Time complexity: O(n), space complexity: O(1)

from linked_list import Node
from linked_list import LinkedList

def calculate_length(llist):
    """Calculate length of linked list."""

    length = 0
    node = llist.head
    while node is not None:
        length += 1
        node = node.next
    return length


def recursive_check_palindrome(length, node):
    "Recursively checks for the palindrome."

    if (length == 1):
        return [True, node.next]
    elif (length == 0):
        return [True, node]
    
    current_node = node

    boolean, opposite_node = recursive_check_palindrome(length - 2, node.next)

    if (opposite_node.data == current_node.data) and boolean:
        return [True, opposite_node.next]
    else:
        return [False, opposite_node.next]


def check_palindrome(llist):
    length = calculate_length(llist)
    node = llist.head
    return recursive_check_palindrome(length, node)[0]


if __name__ == "__main__":
    llist = LinkedList([1, 2, 3, 2, 1])
    print(check_palindrome(llist))

    llist = LinkedList([1, 2, 3, 3, 2, 1])
    print(check_palindrome(llist))

    llist = LinkedList([1, 2, 3, 3, 2, 31])
    print(check_palindrome(llist))

    llist = LinkedList([1, 23, 2, 3, 3, 2, 23, 1])
    print(check_palindrome(llist))