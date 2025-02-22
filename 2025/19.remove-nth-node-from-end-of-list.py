#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (47.87%)
# Likes:    19627
# Dislikes: 840
# Total Accepted:    3.3M
# Total Submissions: 6.8M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1], n = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2], n = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 
# 
# 
# Follow up: Could you do this in one pass?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        find length in first iteration
        '''
        # l = 0
        # temp = head
        # while temp:
        #     temp = temp.next
        #     l += 1

        # pos = l - n

        # if pos < 0: return head
        # if pos == 0: return head.next
        # ans = head
        # pos -= 1
        # while pos > 0:
        #     pos -= 1
        #     head = head.next
        
        # if head and head.next:
        #     head.next = head.next.next
        
        # return ans
        '''
        --------------------------------
        One loop solution
        '''
        ans = head
        temp = ans
        
        while head and n > 0:
            head = head.next
            n -= 1
        
        if not head: return ans.next
        while head and head.next:
            head = head.next
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next
        return ans
        

        
# @lc code=end

