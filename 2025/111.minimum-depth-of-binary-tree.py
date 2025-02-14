#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (49.85%)
# Likes:    7470
# Dislikes: 1326
# Total Accepted:    1.4M
# Total Submissions: 2.7M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^5].
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
        use of dfs
        '''
        # if not root: return 0
        
        # if not root.left and not root.right:
        #     return 1
        # if not root.left:
        #     left_ = math.inf
        # else:
        #     left_ = self.minDepth(root.left)

        # if not root.right:
        #     right_ = math.inf
        # else:
        #     right_ = self.minDepth(root.right)
        # return 1 + min(left_, right_)

        '''
        BFS
        '''

        if not root: return 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        
        
# @lc code=end

