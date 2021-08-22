# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None
        first = self.sortList(head)
        second = self.sortList(start)
        return self.merge(first, second)

        
    def merge(self, l, r):
        if not l:
            return r
        if not r:
            return l
        dummy = ListNode()
        t = dummy
        while l and r:
            if l.val < r.val:
                t.next = l
                l = l.next
            else:
                t.next = r
                r = r.next
            t = t.next
        t.next = l or r
        return dummy.next


