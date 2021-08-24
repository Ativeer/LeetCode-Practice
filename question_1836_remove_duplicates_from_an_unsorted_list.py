from collections import defaultdict
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        hash_set = defaultdict(int)
        h = head
        dummy = ListNode()
        
        dummy.next = head
        ans = dummy
        while head:
            hash_set[head.val] += 1
            head = head.next
        copy = False
        while h:
            if hash_set[h.val] == 1:
                copy = False
                dummy.next = h
                dummy = dummy.next
            else:
                copy = True
                
            h = h.next
        
        if copy:
            dummy.next = None
        return ans.next