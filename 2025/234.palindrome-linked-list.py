#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (54.96%)
# Likes:    17128
# Dislikes: 918
# Total Accepted:    2.3M
# Total Submissions: 4.2M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
# 
# 
# 
# Follow up: Could you do it in O(n) time and O(1) space?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow_ptr = fast_ptr = head
        prev = None

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            # reverse for slow_ptr
            temp = slow_ptr.next
            slow_ptr.next = prev            
            prev = slow_ptr
            slow_ptr = temp

        if fast_ptr:
            # odd number so no need to check for curr_ptr
            slow_ptr = slow_ptr.next

        while slow_ptr and prev:
            if slow_ptr.val != prev.val:
                return False
            slow_ptr = slow_ptr.next
            prev = prev.next
        return True



# @lc code=end

