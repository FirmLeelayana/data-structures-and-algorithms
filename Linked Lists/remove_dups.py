# Given an unsorted linked list, write a method to remove duplicates. Assume a temporary buffer cannot be used.
# Time complexity: O(n^2), space complexity: O(1)

from linked_list import Node
from linked_list import LinkedList

def remove_duplicates(llist):
    """Removes duplicates from a linked list. Returns a modified linked list object.
    
    Input: linked list object
    Output: linked list object
    """

    if llist.head is None:
        return llist

    current = llist.head

    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    
    return llist


if __name__ == "__main__":
    print(remove_duplicates(LinkedList(["a", "b", "a"])))
    print(remove_duplicates(LinkedList(["a", "a", "a"])))
    print(remove_duplicates(LinkedList(["a", "b", "c", "d", "a", "b", "e", "e"])))