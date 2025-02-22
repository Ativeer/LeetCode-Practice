#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (41.67%)
# Likes:    7299
# Dislikes: 3482
# Total Accepted:    928.9K
# Total Submissions: 2.2M
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Note: You must not use any built-in BigInteger library or convert the inputs
# to integer directly.
# 
# 
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Constraints:
# 
# 
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Do not use big int or long
        # Python is weird and it will allog integer to overflow
        # Solution: store the results in an array

        if num1 == "0" or num2 == "0": return "0"

        l1 = len(num1)
        l2 = len(num2)
        res = [0 for _ in range(l1+l2)]

        for i in range(l1-1, -1, -1):
            digit1 = int(num1[i])

            for j in range(l2-1, -1, -1):                
                digit2 = int(num2[j])

                curr_ptr = i + j + 1
                carry_over_ptr = i + j

                mul = digit1 * digit2
                curr_num = mul + res[curr_ptr]
                correct_num = curr_num % 10
                carry = curr_num // 10

                res[curr_ptr] = correct_num
                res[carry_over_ptr] += carry

        ans = ""
        start_ptr = 0
        for i in range(len(res)):
            if res[i] != 0:
                start_ptr = i
                break
        for i in range(start_ptr, len(res)):
            ans += str(res[i])
        return ans

# @lc code=end

