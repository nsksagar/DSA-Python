class Node:

    def __init__(self,val):

        self.val = val 
        self.left = None 
        self.right = None 


    
root = Node(1)

root.left = Node(2)

root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)


def print_pre_order(node):

    if not node:
        return 
    
    print(node.val, end = ' ')

    print_pre_order(node.left)
    print_pre_order(node.right)


print('Pre-order traversal : ')

print_pre_order(root)

print('\n')
def inorder(node):

    if not node:
        return 
    
    inorder(node.left)
    print(node.val, end = ' ')
    inorder(node.right)

print('In-order Traversal :')
inorder(root)

print('\n')

def postorder(node):

    if not node:
        return 
    
    postorder(node.left)
    postorder(node.right)
    print(node.val , end = ' ')


print('Post-order Traversal :')
postorder(root)