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
        return self.stack

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
        return self.queue

    def __iter__(self):
        for item in self.queue:
            yield item
