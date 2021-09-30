# Create a class that takes in a set of stacks.

from stack_queue import Stack

class SetOfStacks:

    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [Stack([])]

    def get_latest_stack(self):
        return self.stacks[-1]
    
    def check_latest_stack_full(self):
        latest_stack = self.get_latest_stack()
        return (latest_stack.size() == self.capacity)
    
    def pop(self):
        latest_stack = self.get_latest_stack()
        if latest_stack.size() == 1:
            latest_stack.pop()
            self.stacks.pop()
        elif (latest_stack is not None):
            latest_stack.pop()

    def push(self, item):
        latest_stack = self.get_latest_stack()
        if not self.check_latest_stack_full():
            latest_stack.push(item)
        else:
            new_stack = Stack()
            self.stacks.append(new_stack)
            latest_stack = self.get_latest_stack()
            latest_stack.push(item)

    def output(self):
        list = []
        for st in self.stacks:
            list.append(" | ")
            list.extend(st.stack)
        print(" / ".join(list))


if __name__ == "__main__":
    set_of_stacks = SetOfStacks(3)
    set_of_stacks.push('a')
    set_of_stacks.output()
    set_of_stacks.push('a')
    set_of_stacks.output()
    set_of_stacks.push('a')
    set_of_stacks.output()
    set_of_stacks.push('a')
    set_of_stacks.output()

    
    

