# Sort a stack such that the minimum value shows up on top. A temporary stack buffer may be used.
# Time complexity: O(n^2), space complexity: O(n)

from stack_queue import Stack

def sort_stack(input_stack):
    """Sorts a stack implementation, with minimum values at the top."""
    
    temp_stack = Stack()

    while input_stack.peek() is not None:
        latest_variable = input_stack.pop()
        if temp_stack.peek() is None:
            temp_stack.push(latest_variable)
        else:
            while temp_stack.size() > 0:
                top_variable = temp_stack.peek()
                if latest_variable >= top_variable:
                    temp_stack.push(latest_variable)
                    break
                else:
                    temp_variable = temp_stack.pop()
                    input_stack.push(temp_variable)
            if temp_stack.size() == 0: # Accounting for if it is the smallest value there
                temp_stack.push(latest_variable)

    while temp_stack.peek() is not None:
        latest_variable = temp_stack.pop()
        input_stack.push(latest_variable)

    return input_stack


if __name__ == "__main__":
    input_stack = Stack([1, 2, 5, 2])
    print(input_stack)

    input_stack = sort_stack(input_stack)
    print(input_stack)

    input_stack = Stack([3, 2, 5, 23, 52, 3, 6])
    print(input_stack)

    input_stack = sort_stack(input_stack)
    print(input_stack)