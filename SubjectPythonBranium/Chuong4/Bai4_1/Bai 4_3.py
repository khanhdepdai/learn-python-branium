def push_stack(stack, data):
    # This function push item into stack
    return stack.append(data)


def is_empty(stack):
    # This function check stack is empty or not emtpy
    return len(stack) == 0


def pop_stack(stack):
    # This function return and remove top element of stack
    if is_empty():
        return None
    return stack.pop()


def peek_stack(stack):
    # This function return top element of stack
    if is_empty():
        return None
    return stack[len(stack) - 1]


def size_stack(stack):
    # This function return size of stack
    return len(stack)


def insert_stack(stack, data, position):
    # This function insert item into stack with position
    return stack.insert(position, data)


def check_position_add(stack, value):
    # This function check position if add value in ascending
    for i in range(len(stack)):
        if value < stack[i]:
            return i
    return True # return True, call function push_stack


def save_stack_asc(stack, list):
    # This function save data from list to stack in ascending order
    for i in range(len(list)):
        if i == 0:
            push_stack(stack, list[0])
        else:
            pos = check_position_add(stack, list[i])  # pos = position need insert
            if pos is True:
                push_stack(stack, list[i])
            elif pos is not True:
                stack.insert(pos, list[i])

    return stack


stack = []
print(save_stack_asc(stack, [3, 2, 61234, 1, -2, 0, 1, 3, 1, 5, -2324, -131]))
