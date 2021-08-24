# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        t = dummy
        prev = False
        while head:
            if head.next and head.val == head.next.val:
                prev = True
            elif prev:
                if head.next:
                    prev = False
                else:
                    t.next = None
                    break
            else:
                t.next = head
                t = t.next
            head = head.next
        
        return dummy.next