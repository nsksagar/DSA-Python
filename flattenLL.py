# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:

    def sorting(self,l1,l2):

        dummynode = ListNode(-1, None, None)
        curr = dummynode

        curr1 = l1
        curr2 = l2 

        if curr1:
            curr1.next = None

        while curr1 and curr2:
            if curr1.val >= curr2.val:
                curr.child = curr2
                curr2 = curr2.child
            else:
                curr.child = curr1
                curr1 = curr1.child 
            curr = curr.child
            curr.next = None

        if curr1:
            curr.child = curr1

        else:
            curr.child = curr2

        return dummynode.child

    def flattenLinkedList(self, head):

        if not head or head.next is None:
            return head 

        
        mergedhead = self.flattenLinkedList(head.next)
        
        return self.sorting(head,mergedhead)

        