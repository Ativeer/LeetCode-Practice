#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
def bToDLL(root):
    # do Code here
    head = None
    p = None
    curr = root
    while curr:
        if not curr.left:
            if p:
                p.right = curr
            
            curr.left = p
            p = curr
            
            if not head:
                head = curr
            curr = curr.right
     
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
            
            if prev.right == curr:
                curr.left = p
                p = curr
                curr = curr.right
            else:
                prev.right = curr
                curr = curr.left
    return head
