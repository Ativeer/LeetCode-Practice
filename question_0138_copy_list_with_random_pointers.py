"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        random = {}
        og_to_new = {}
        dummy = Node(-1)
        new_node = dummy
        temp = head
        while head:
            random[head] = head.random
            n = Node(head.val)
            new_node.next = n
            new_node = new_node.next
            og_to_new[head] = n
            head = head.next
        last_node = new_node.next
        temp2 = dummy.next
        while temp2:
            if random[temp] is None:
                random_pointer = last_node
            else:
                random_pointer = og_to_new[random[temp]]
            temp2.random = random_pointer
            temp2 = temp2.next
            temp = temp.next
        return dummy.next
            