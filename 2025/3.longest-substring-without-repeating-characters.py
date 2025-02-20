#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (36.16%)
# Likes:    41280
# Dislikes: 1991
# Total Accepted:    7M
# Total Submissions: 19.3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without duplicate
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        start_window = 0
        end_window = 1

        ans = 1
        letters_in_window = set()
        letters_in_window.add(s[0])

        while end_window < len(s):
            curr_char = s[end_window]
            if curr_char not in letters_in_window:
                end_window += 1
                letters_in_window.add(curr_char)
                ans = max(ans, len(letters_in_window))                
            else:

                while start_window < end_window and s[start_window] != curr_char:
                    letters_in_window.remove(s[start_window])
                    start_window += 1
                    
                start_window += 1
                end_window += 1


        return ans


# @lc code=end

