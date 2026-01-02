
def reverse_stack(stack):

    if not stack:
        return 
    temp = stack.pop()
    reverse_stack(stack)
    insertatBottom(stack,temp)


def insertatBottom(stack, item):

    if not stack:
        stack.append(item)
        return 

    temp = stack.pop()
    insertatBottom(stack, item)

    stack.append(temp)


if __name__ == '__main__':

    stack = [1,2,3,4,5,6]
    print(f'Actual stack is {stack}')

    reverse_stack(stack)

    print(f'Reversed stack is {stack}')

    

    