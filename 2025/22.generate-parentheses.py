#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.36%)
# Likes:    21843
# Dislikes: 1014
# Total Accepted:    2.2M
# Total Submissions: 2.9M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(temp="", open_count=0, close_count=0):
            if len(temp) == 2*n:
                ans.append(temp)
                return
            
            if open_count < n:
                backtrack(temp+"(", open_count+1, close_count)

            if close_count < open_count:
                backtrack(temp+")", open_count, close_count+1)
        backtrack()
        return ans

# @lc code=end

