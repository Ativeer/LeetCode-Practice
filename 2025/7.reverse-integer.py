#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Medium (29.75%)
# Likes:    13825
# Dislikes: 13723
# Total Accepted:    3.8M
# Total Submissions: 12.9M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
# 
# 
# Example 1:
# 
# 
# Input: x = 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: x = -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: x = 120
# Output: 21
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        newNum = abs(x)
        res = 0

        while newNum:
            rem = newNum % 10
            if res > ((2**31) - 1)/10 - rem + 1:
                return 0

            res *= 10
            res += rem
            newNum //= 10

        return res if x >0 else -res
# @lc code=end

