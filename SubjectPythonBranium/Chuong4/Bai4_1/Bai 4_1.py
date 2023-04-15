def push_stack(stack, data):
    # This function push new item into stack
    return stack.append(data)

def is_empty(stack):
    # This function check stack is empty or not empty
    return len(stack) == 0


def pop_stack(stack):
    # This function return and remove top element of stack
    if is_empty(stack):
        return None
    return stack.pop()


def peek_stack(stack):
    # This function return top element of stack
    if is_empty(stack):
        return None
    return stack[len(stack) - 1]


def size_stack(stack):
    # This function return len of stack
    if is_empty(stack):
        return None
    return len(stack)


def reverse_string(s): # s is original string
    # This function return convert of original string
    stack = []
    new_str = ""
    for i in range(len(s)):
        push_stack(stack, s[i])
    for i in range(len(s)):
        new_str += pop_stack(stack)
    return new_str

s = "khanh dep dai lam roi"
t = reverse_string(s)
print(t)
