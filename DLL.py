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

def del_head_DLL(head):

    if not head:
        return head 
    
    if head.next is None:
        return None 

    curr = head 
    head = head.next 
    head.prev = None   
    curr.next = None 


    return head


def del_tail_dll(head):

    if not head:
        return None 
    
    if head.next is None:
        return None 
    

    tail = head

    while tail.next:
        tail = tail.next 

    tail.prev.next = None

    tail.prev = None

    return head 

def del_kth_element(head, k):

    if not head:
        return None 
    
    count = 0
    temp = head 
    while temp is not None:
        count += 1
        if count == k:
            break 
        temp = temp.next

    back = temp.prev 
    front = temp.next 

    if back == None and front == None:
        return None 
        
    elif back == None:
        del_head_DLL(temp)
        return 
    elif front == None:
        del_tail_dll(temp)
        return 
    else:
        back.next = front 
        front.prev = back
        temp.next = None 
        temp.prev = None 
    return head

def remove_giv_node(temp):

    back = temp.prev
    front = temp.next

    if front == None: 
        back.next = None
        temp.prev = None

    back.next = front
    front.prev = back 
    temp.next = None 
    temp.prev = None 


if __name__ == '__main__':

    array = [10,20,30,40,50]

    print(f"Original Array: {array}\n")

    dll_head = convert_arr_to_dll(array)


    print_dll(dll_head)

    #rem_tail = del_tail_dll(dll_head)
    #print_dll(rem_tail)

    #rem_kth = del_kth_element(dll_head, 3)
    #print_dll(rem_kth)

    del_node = remove_giv_node(dll_head.next.next)
    print_dll(dll_head)

    #remove_head = del_head_DLL(dll_head)
    #print_dll(remove_head)

