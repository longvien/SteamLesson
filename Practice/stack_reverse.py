def reverse(stack):
    new_stack = Stack()
    while not stack.is_empty():
        new_stack.push(stack.pop())
    stack = new_stack