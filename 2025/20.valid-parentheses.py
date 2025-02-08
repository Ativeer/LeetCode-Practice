#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # use stack to maintain the order of brackets
        stack = []
        brackets_dict = {")":"(",
                         "}":"{",
                         "]":"["}
        for bracket in s:
            if bracket in brackets_dict:
                if not stack or stack[-1] != brackets_dict[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        return stack == []

# @lc code=end

