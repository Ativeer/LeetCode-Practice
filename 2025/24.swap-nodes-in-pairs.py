#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (66.32%)
# Likes:    12330
# Dislikes: 470
# Total Accepted:    1.6M
# Total Submissions: 2.4M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# 
# Output: [2,1,4,3]
# 
# Explanation:
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = []
# 
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1]
# 
# Output: [1]
# 
# 
# Example 4:
# 
# 
# Input: head = [1,2,3]
# 
# Output: [2,1,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        prev = ListNode()
        curr = head
        prev.next = head
        ans = prev

        while curr and curr.next:
            far = curr.next.next
            next_ = curr.next
            
            curr.next = far
            next_.next = curr
            prev.next = next_

            prev = curr
            curr = far
        return ans.next
    



# @lc code=end

