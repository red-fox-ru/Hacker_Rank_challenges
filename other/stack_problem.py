# HackerRank Java Stack problem


# Create a stack that can handle the following operations:

# "push k": Move k to the top of the stack
# "pop": Remove the topmost element from the stack
# "inc e k": Add 'k' to the bottom 'e' elements of the stack.

# The pop function is never called on an empty stack.
# If the stack is empty at any point, print "EMPTY".

# Example:
# ops = ["push 4", "pop", "push 3", "push 5", "push -1", "inc 1 5", "pop"].


def create_stack(ops: list):
    stack = []
    if ops is None or len(ops) == 0:
        print("EMPTY")
        return None

    for current in ops:
        if 'pop' in current:
            stack.pop()
            if len(stack) < 1:
                print("EMPTY")
        if 'push' in current:
            stack.append(int(current[-1]))
        if 'inc' in current:
            e, k = current.split()[1:]
            for item in range(len(stack)):
                if item < int(e):
                    stack[item] += int(k)
    return stack


if __name__ == '__main__':
    create_stack(['push 4', 'pop', 'push 3', 'push 5', 'inc 2 1', 'pop', 'push 5', 'push -1', 'inc 1 5', 'pop'])
