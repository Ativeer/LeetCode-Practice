#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (35.15%)
# Likes:    30291
# Dislikes: 1867
# Total Accepted:    3.6M
# Total Submissions: 10.2M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]

        def check_for_palindrome(start, end, string):
            while start >= 0 and end < len(string) and string[start] == string[end]:
                start -= 1
                end += 1
            return string[start+1: end]
        
        for i in range(len(s)-1):
            # odd length check
            odd_palindrom_str = check_for_palindrome(i, i, s)
            if len(ans) < len(odd_palindrom_str):
                ans = odd_palindrom_str
            even_palindrom_str = check_for_palindrome(i, i+1, s)
            if len(ans) < len(even_palindrom_str):
                ans = even_palindrom_str
        return ans
            
# @lc code=end

