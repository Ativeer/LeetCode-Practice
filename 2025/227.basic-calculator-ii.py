#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (45.08%)
# Likes:    6333
# Dislikes: 898
# Total Accepted:    774.2K
# Total Submissions: 1.7M
# Testcase Example:  '"3+2*2"'
#
# Given a string s which represents an expression, evaluate this expression and
# return its value. 
# 
# The integer division should truncate toward zero.
# 
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2^31, 2^31 - 1].
# 
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
# 
# 
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# Example 2:
# Input: s = " 3/2 "
# Output: 1
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by some
# number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0,
# 2^31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.
# 
# 
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operation = {"*", "/", "+", "-"}
        ptr = 0

        def operation_task(operation_, input, pointer):
            if operation_ in "+-":
                stack.append(operation_)
                return pointer

            # now same method for multiplying or division
            prev_ = 0
            prev_number = stack.pop()
            while pointer < len(input) and input[pointer] not in operation:
                if input[pointer] == " ":
                    pointer += 1
                    continue
                prev_ *= 10
                prev_ += int(input[pointer])
                pointer += 1
            
            if operation_ == "*":
                stack.append(prev_number * prev_)
            else:
                stack.append(prev_number // prev_)
            
            return pointer

        while ptr < len(s):
            ch = s[ptr]
            # for spaces
            if ch == " ": 
                ptr += 1
                continue
            # if a operation is detected
            if ch in operation:
                # do something in operation method
                ptr = operation_task(ch, s, ptr+1)
            else:
                # a number is found
                prev_num = 0
                if stack and stack[-1] not in operation:
                    prev_num = stack.pop()
                prev_num *= 10
                prev_num += int(ch)
                stack.append(prev_num)
                ptr += 1

            

        ans = 0
        stack = stack[::-1]
        while stack:
            last_activity = stack.pop()
            if isinstance(last_activity, str):
                following_num = stack.pop()
                if last_activity == "+":
                    ans += following_num
                else:
                    ans -= following_num
            else:
                ans += last_activity
        return ans        

# @lc code=end

