class Node:
    def __init__(self, data):

        self.data = data
        self.next = None 
        self.prev = None


def convert_arr_to_dll(array):

    if not array:
        return None 
    
    head = Node(array[0])
    curr = head

    for item in array[1:]:

        new_node = Node(item)
        curr.next = new_node
        new_node.prev = curr

        curr = new_node

    return head

def print_dll(head):

    if not head:
        print('Empty list')
        return 

    print('---Forward Pass---')
    curr = head 
    while curr:
        print(curr.data, end = '->')
        tail = curr
        curr = curr.next 
    print(None)

    print('---Backward Pass---')

    while tail:
        print(tail.data, end = '->')
        tail = tail.prev

    print(None)



if __name__ == '__main__':

    array = [10,20,30,40,50]

    print(f"Original Array: {array}\n")

    dll_head = convert_arr_to_dll(array)


    print_dll(dll_head)



