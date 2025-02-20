#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (45.22%)
# Likes:    32859
# Dislikes: 6600
# Total Accepted:    5.4M
# Total Submissions: 12M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = temp = ListNode()
        
        while l1 and l2:
            
            val = l1.val + l2.val + carry
            carry = val // 10
            val = val % 10
            new_node = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            temp.next = new_node
            temp = temp.next
        
        while l1:
            val = l1.val + carry
            carry = val // 10
            val = val % 10
            new_node = ListNode(val)
            l1 = l1.next
            temp.next = new_node
            temp = temp.next
        
        while l2:
            val = l2.val + carry
            carry = val // 10
            val = val % 10
            new_node = ListNode(val)
            l2 = l2.next
            temp.next = new_node
            temp = temp.next
        
        if carry == 1:
            temp.next = ListNode(1)
        return ans.next


# @lc code=end

