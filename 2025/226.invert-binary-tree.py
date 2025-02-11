#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (78.47%)
# Likes:    14398
# Dislikes: 238
# Total Accepted:    2.5M
# Total Submissions: 3.1M
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Given the root of a binary tree, invert the tree, and return its root.
# 
# 
# Example 1:
# 
# 
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# 
# 
# Example 2:
# 
# 
# Input: root = [2,1,3]
# Output: [2,3,1]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        left_ = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left_)
        return root


# @lc code=end

