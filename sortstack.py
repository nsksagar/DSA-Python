
def insert(stack, temp):

    if not stack or stack[-1] <= temp:
        stack.append(temp)
        return
    
    val = stack.pop()
    insert(stack, temp)
    stack.append(val)

def sort_stack(stack):

    if stack:
        temp = stack.pop()
        sort_stack(stack)
        insert(stack, temp)


if __name__ == '__main__':

    stack = [32, 18 ,42, 8 , 4 ,9, 25]

    print('Original Stack:' , stack)
    sort_stack(stack)
    print("Sorted stack:",  stack)