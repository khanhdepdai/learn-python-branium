def push_stack(stack, data):
    # This function push item into stack
    return stack.append(data)


def is_empty(stack):
    # This function ckeck stack is empty or not empty
    return len(stack) == 0


def pop_stack(stack):
    # This function return and remove top of stack
    if is_empty(stack):
        return None
    return stack.pop()


def peek_stack(stack):
    # This function return top of stack
    if is_empty(stack):
        return None
    return stack[len(stack) - 1]


def size_stack(stack):
    # This function check size of stack
    return len(stack)


def check_summetry(arr):
    # This function is check summetry
    len_arr = len(arr)
    stack = []
    for i in range(len_arr):
        push_stack(stack, arr[i])
    for i in range(len_arr):
        top_stack = pop_stack(stack)
        if arr[i] != top_stack:
            return False
    return True


arr1 = [1, 2, 3, 3, 5, 4, 3, 2, 1]
arr2 = [6, 7, 8, 9, 9, 8, 7, 6]
arr3 = [23, 312, 5, 3, 1, 4]
print(check_summetry(arr1))
print(check_summetry(arr2))
print(check_summetry(arr3))
