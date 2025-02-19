#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (61.32%)
# Likes:    5582
# Dislikes: 313
# Total Accepted:    682.8K
# Total Submissions: 1.1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the sum of all left leaves.
# 
# A leaf is a node with no children. A left leaf is a leaf that is the left
# child of another node.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and
# 15 respectively.
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = [(root, "")]
        ans = 0
        while q:
            total_nodes_at_level = len(q)
            for i in range(total_nodes_at_level):
                node, parent = q.pop(0)
                if not node.left and not node.right:
                    if parent == "left":
                        ans += node.val
                if node.left:
                    q.append((node.left, "left"))
                if node.right:
                    q.append((node.right, "right"))
        return ans


            
        
# @lc code=end

