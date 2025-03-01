#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (42.28%)
# Likes:    8499
# Dislikes: 473
# Total Accepted:    909.3K
# Total Submissions: 2.1M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
# 
# 
# Example 1:
# 
# 
# Input: s = "aba"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# 
# 
# Example 3:
# 
# 
# Input: s = "abc"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def __isPalindrome(start, end):
            while start <= end and s[start] == s[end]:
                start += 1
                end -= 1
            return (start > end), start, end

        check, start, end = __isPalindrome(0, len(s)-1)
        if not check:
            check1, _, _ = __isPalindrome(start+1, end)
            check2, _, _ = __isPalindrome(start, end-1)
            return check1 or check2
        return True

        
# @lc code=end

