#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (35.99%)
# Likes:    12257
# Dislikes: 4557
# Total Accepted:    1.4M
# Total Submissions: 3.9M
# Testcase Example:  '"12"'
#
# You have intercepted a secret message encoded as a string of numbers. The
# message is decoded via the following mapping:
# 
# "1" -> 'A'
# "2" -> 'B'
# ...
# "25" -> 'Y'
# "26" -> 'Z'
# 
# However, while decoding the message, you realize that there are many
# different ways you can decode the message because some codes are contained in
# other codes ("2" and "5" vs "25").
# 
# For example, "11106" can be decoded into:
# 
# 
# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only
# "6" is valid).
# 
# 
# Note: there may be strings that are impossible to decode.
# 
# Given a string s containing only digits, return the number of ways to decode
# it. If the entire string cannot be decoded in any valid way, return 0.
# 
# The test cases are generated so that the answer fits in a 32-bit integer.
# 
# 
# Example 1:
# 
# 
# Input: s = "12"
# 
# Output: 2
# 
# Explanation:
# 
# "12" could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: s = "226"
# 
# Output: 3
# 
# Explanation:
# 
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# 
# 
# Example 3:
# 
# 
# Input: s = "06"
# 
# Output: 0
# 
# Explanation:
# 
# "06" cannot be mapped to "F" because of the leading zero ("6" is different
# from "06"). In this case, the string is not a valid encoding, so return
# 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).
# 
# 
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:

        '''
        DP:
        C[i] = C[i-1] + C[i-2]
        given ith index is a valid single digit and double digit

        if only single digit:
        C[i] = C[i-1]

        if only double digit:
        C[i] = C[i] + C[i-2]
        '''

        def  __isValid(ptr=1):
            if ptr == len(s): return False
            if s[ptr-1] == "0" or (s[ptr-1] != "1" and s[ptr-1] != "2"): return False
            return int(s[ptr-1:ptr+1]) < 27
        
        dp = [0 for _ in range(len(s)+1)]
        if s[0] == "0": return 0
        dp[0] = 1
        dp[1] = 1

        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i+1] = dp[i]

            elif not __isValid(i):
                return 0
                
            if __isValid(i):
                dp[i+1] += dp[i-1]

        return dp[-1]

        '''
        Backtracking yields TLE for
        "111111111111111111111111111111111111111111111"
        '''
        # count = 0

        # def backtrack(ptr=0):
        #     if ptr == len(s):
        #         nonlocal count
        #         count += 1
        #         return
            
        #     # include just this one
        #     if s[ptr] != "0":
        #         backtrack(ptr+1)
            
        #     # check if the current number can be included as 2 numbers
        #     if __isValid(ptr):
        #         backtrack(ptr+2)
                
        # backtrack()
        # return count


# @lc code=end

