# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.sum = []
        
        def traverse(node, sum_so_far=0):
            if not node:
                return 0
            
            left = traverse(node.left)
            right = traverse(node.right)
            self.sum.append(node.val + left + right)
            return node.val + left + right
        
        traverse(root)
        m = 0
        s = self.sum[-1]
        for i in self.sum:
            m = max(m, i * (s - i))   
        return m % (10 ** 9 + 7)