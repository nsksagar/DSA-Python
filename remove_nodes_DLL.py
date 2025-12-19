# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):

        # remove head 
        def remove_head(head):
            if not head or head.next is None: 
                return None
            temp = head 
            head = head.next 
            temp.next = None 
            head.prev = None 
            return head

        # remove tail 
        def remove_tail(tail):
            new_tail = tail.prev 
            tail.prev = None 
            new_tail.next = None 

        # remove any other element 
        def remove_element(node):
            anch_node = node.prev
            node.next.prev = anch_node
            anch_node.next = node.next 
            node.next = None 
            node.prev = None 


        curr = head 

        if not head:
            return None 

        if head.next is None:
            if head.val == target: 
                return None
            else: 
                return head
        
        while curr is not None: 
            next_node = curr.next
            if curr.val == target:

                if curr.prev is None: 
                    head = remove_head(curr)
                elif curr.next is None: 
                    remove_tail(curr)
                else:
                    remove_element(curr)
            curr = next_node

        return head
    

#### Another solution using dummy head
            
# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):

        dummy_head = ListNode(0, head, None)

        if head: 
            head.prev = dummy_head

        curr = head 

        while curr: 

            next_node = curr.next 

            if curr.val == target: 

                prev_node = curr.prev
                prev_node.next = next_node

                if next_node:
                    next_node.prev = prev_node
            
            
                    curr.next = None
                    curr.prev = None

            
            curr = next_node


        new_head = dummy_head.next
        if new_head:
            new_head.prev = None 
        
        return new_head
             
            

