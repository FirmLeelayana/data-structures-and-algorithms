# Implementation of simple stack and queue data structures.

class Stack:
    """Simple implementation of a stack class."""

    def __init__(self, stack = []):
        self.stack = stack

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if len(self.stack) < 1:
            return None
        else:
            return self.stack[-1]
    
    def is_empty(self):
        return (len(self.stack) < 1)

    def size(self):
        return len(self.stack)

    def __repr__(self):
        return "->".join(self.stack)

    def __iter__(self):
        for item in self.stack:
            yield item


class Queue:
    """Simple implementation of a queue class."""

    def __init__(self, queue = []):
        self.queue = queue

    def enqueue(self, item):
        self.queue.append(item) 
    
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue[-1]

    def is_empty(self):
        return (len(self.queue) < 1)

    def size(self):
        return len(self.queue)

    def __repr__(self):
        return " -> ".join(self.queue)

    def __iter__(self):
        for item in self.queue:
            yield item


if __name__ == "__main__":
    my_stack = Stack(['a', 'b', 'c'])
    print(my_stack)

    my_stack.pop()
    print(my_stack)

    my_stack.push('d')
    print(my_stack)
    print(my_stack.peek())
    print(my_stack.is_empty())
    print(my_stack.size())

    my_queue = Queue(['a', 'b', 'c'])
    print(my_queue)

    my_queue.dequeue()
    print(my_queue)

    my_queue.enqueue('d')
    print(my_queue)
    print(my_queue.peek())
    print(my_queue.is_empty())
    print(my_queue.size())