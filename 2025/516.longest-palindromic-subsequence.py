#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (63.56%)
# Likes:    9819
# Dislikes: 332
# Total Accepted:    586.3K
# Total Submissions: 921.2K
# Testcase Example:  '"bbbab"'
#
# Given a string s, find the longest palindromic subsequence's length in s.
# 
# A subsequence is a sequence that can be derived from another sequence by
# deleting some or no elements without changing the order of the remaining
# elements.
# 
# 
# Example 1:
# 
# 
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        recurssion
        '''
        # return self.__recurse(s, 0, len(s)-1)
        '''
        Memoization
        '''
        # memo = [[0 for _ in range(len(s))] for _ in range(len(s))]
        # return self.__memoization(memo, 0, len(s)-1, s)

        return self.__tabulationDp(s)
    
    def __tabulationDp(self, s):
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(len(s)-i):
                ind = j + i
                if i == 0:
                    dp[j][ind] = 1
                elif i == 1:
                    if s[j] == s[ind]:
                        dp[j][ind] = 2
                    else:
                        dp[j][ind] = 1
                else:
                    if s[j] == s[ind]:
                        dp[j][ind] = 2 + dp[j+1][ind-1]
                    else:
                        dp[j][ind] = max(dp[j+1][ind], dp[j][ind-1])
        return dp[0][-1]
        

    def __memoization(self, memo, left_index, right_index, s):
        if left_index > right_index:
            return 0
        if left_index == right_index:
            return 1
        
        if memo[left_index][right_index]:
            return memo[left_index][right_index]
        if s[left_index] == s[right_index]:
            memo[left_index][right_index] = 2 + self.__memoization(memo, left_index+1, right_index-1, s)
            return memo[left_index][right_index]
        memo[left_index][right_index] = max(self.__memoization(memo, left_index+1, right_index, s),
                                            self.__memoization(memo, left_index, right_index-1, s))
        return memo[left_index][right_index]

    def __recurse(self, s, left_index, right_index):
        if left_index == right_index:return 1
        if left_index > right_index: return 0
        if s[left_index] == s[right_index]: return (2 + self.__recurse(s, left_index+1, right_index-1))
        return max(self.__recurse(s, left_index+1, right_index), self.__recurse(s, left_index, right_index-1))

# @lc code=end

