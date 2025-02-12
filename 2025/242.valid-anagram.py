#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (66.01%)
# Likes:    12724
# Dislikes: 422
# Total Accepted:    4.4M
# Total Submissions: 6.7M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ctr = Counter(s)
        t_ctr = Counter(t)

        for i in s_ctr:
            if i not in t_ctr or s_ctr[i] != t_ctr[i]:
                return False
            
        for i in t_ctr:
            if i not in s_ctr or s_ctr[i] != t_ctr[i]:
                return False
        return True
        
# @lc code=end

