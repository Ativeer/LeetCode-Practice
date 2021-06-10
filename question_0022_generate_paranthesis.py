from collections import defaultdict
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(stack=[], c1=0, c2=0):
            if len(stack) == 2*n:
                ans.append("".join(stack))
                return
            if c1 < n:
                stack.append("(")
                helper(stack, c1+1, c2)
                stack.pop()
            
            if c2 < c1:
                stack.append(")")
                helper(stack, c1, c2+1)
                stack.pop()
            
        helper()
        return ans