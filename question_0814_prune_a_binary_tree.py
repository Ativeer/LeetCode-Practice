# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def check(root):
            if not root:
                return True
            leftVal = check(root.left)
            rightVal = check(root.right)
            if root.val == 1:
                if leftVal:
                    root.left = None
                if rightVal:
                    root.right = None
                return False
            elif root.val == 0:
                if leftVal:
                    root.left = None
                if rightVal:
                    root.right = None
                if leftVal and rightVal:
                    return True
                return False
        t = check(root)
        return root if not t else None