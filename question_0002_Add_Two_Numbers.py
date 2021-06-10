# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        node = ListNode()
        root = node
        
        while l1 and l2:
            newnode = ListNode()
            node.next = newnode
            node = node.next
            val = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next
            node.val = val%10
            carry = val // 10
            
        while l1:
            newnode = ListNode()
            node.next = newnode
            node = node.next
            val = l1.val + carry
            l1 = l1.next
            node.val = val%10
            carry = val//10
                    
        while l2:
            newnode = ListNode()
            node.next = newnode
            node = node.next
            val = l2.val + carry
            l2 = l2.next
            node.val = val%10
            carry = val//10
        
        if carry > 0:
            newnode = ListNode()
            node.next = newnode
            node = node.next
            node.val = carry
            
        
        return root.next