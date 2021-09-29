class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, nodes=None):
        # Creating linked list
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(str(node.data))
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        # Traversing linked list
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        # Adding node to beginning
        node.next = self.head
        self.head = node

    def add_end(self, node):
        # adding node to the end
        current_node = self.head
        if current_node is None:
            self.head = node
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        

if __name__ == "__main__":
    llist = LinkedList()
    print(llist)

    node_one = Node(13)
    node_two = Node(4)
    node_three = Node(2)
    
    node_one.next = node_two
    node_two.next = node_three

    llist.head = node_one
    print(llist)

    llist_two = LinkedList([2, 3, 4])
    print(llist_two)

    for node in llist:
        print(node)

    llist.add_end(Node("e"))
    print(llist)