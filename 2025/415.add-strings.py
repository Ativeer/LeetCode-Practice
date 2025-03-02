#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (51.69%)
# Likes:    5170
# Dislikes: 782
# Total Accepted:    768.5K
# Total Submissions: 1.5M
# Testcase Example:  '"11"\n"123"'
#
# Given two non-negative integers, num1 and num2 represented as string, return
# the sum of num1 and num2 as a string.
# 
# You must solve the problem without using any built-in library for handling
# large integers (such as BigInteger). You must also not convert the inputs to
# integers directly.
# 
# 
# Example 1:
# 
# 
# Input: num1 = "11", num2 = "123"
# Output: "134"
# 
# 
# Example 2:
# 
# 
# Input: num1 = "456", num2 = "77"
# Output: "533"
# 
# 
# Example 3:
# 
# 
# Input: num1 = "0", num2 = "0"
# Output: "0"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            return self.addStrings(num2, num1)
        
        j = 0

        carry = 0
        ans = ""
        while j < len(num2):
            pos_2 = len(num2) - j - 1
            pos_1 = len(num1) - j - 1
            newNum = int(num1[pos_1]) + int(num2[pos_2]) + carry
            carry = newNum // 10
            newNum = newNum % 10
            ans = str(newNum) +  ans
            j += 1
        
        rem_pos = len(num1) - len(num2)
        
        
        while rem_pos:
            pos_1 = rem_pos-1
            newNum = carry + int(num1[pos_1])
            carry = newNum // 10
            newNum = newNum % 10            
            ans = str(newNum) + ans
            rem_pos -= 1
        if carry:
            ans = "1" + ans
        return ans


        
# @lc code=end

