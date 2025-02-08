#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (64.26%)
# Likes:    11970
# Dislikes: 257
# Total Accepted:    2.6M
# Total Submissions: 4.1M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
# 
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
# 
# 
# Example 1:
# 
# 
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: p = [1,2], q = [1,null,2]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        recurssion
        '''
        # if not p and not q: return True
        # if not p or not q: return False
        # if p.val != q.val: return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        '''
        Iterative
        '''
        if not p and not q: return True
        if not p or not q: return False
        stack = [(p, q)]
        while stack:
            curr_p, curr_q = stack.pop()
            if not curr_p and not curr_q: continue
            if not curr_p or not curr_q: return False
            if curr_p.val != curr_q.val: return False
            stack.append((curr_p.left, curr_q.left))
            stack.append((curr_p.right, curr_q.right))
        return stack == []

# @lc code=end

