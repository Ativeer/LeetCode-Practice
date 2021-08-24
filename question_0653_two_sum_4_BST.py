# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ans = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        
        hashmap = {}
        for val in ans:
            if k-val in hashmap:
                return True
            hashmap[val] = 1
        
        return False


## Approach 2

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ans = set()
        def traversal(node):
            if not node:
                return False
            if (k-node.val) in ans:
                return True
            ans.add(node.val)
            return traversal(node.left) or traversal(node.right)
        return traversal(root)