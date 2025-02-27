#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Medium (58.04%)
# Likes:    15399
# Dislikes: 257
# Total Accepted:    1.1M
# Total Submissions: 1.9M
# Testcase Example:  '"horse"\n"ros"'
#
# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following three operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
# 
# Constraints:
# 
# 
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        backtracking TLE
        '''
        if len(word1) < len(word2):
            return self.minDistance(word2, word1)
        
        # Backtracking yields TLE
        # self.actions = math.inf
        # self.__backtrack(word1, word2, 0)
        # return self.actions
        
        
        self.word1 = word1
        self.word2 = word2
        m = len(self.word1)
        n = len(self.word2)

        self.memo = [[-1 for _ in range(n)] for _ in range(m)]

        return self.__memoizattion(0, 0)


    def __backtrack(self, word1, word2, actions=0):
        if not word1 and not word2:
            self.actions = min(self.actions, actions)
            return
        
        if not word1:
            self.actions = min(actions + len(word2), self.actions)
            return
        
        if not word2:
            self.actions = min(actions + len(word1), self.actions)
            return

        first_char_w1 = word1[0]
        first_char_w2 = word2[0]
        
        if first_char_w1 == first_char_w2:
            self.__backtrack(word1[1:], word2[1:], actions)
        else:
            # remove
            self.__backtrack(word1[1:], word2, actions+1)
            # update
            self.__backtrack(word1[1:], word2[1:], actions+1)
            # insert
            self.__backtrack(word1, word2[1:], actions+1)

    def __memoizattion(self, i, j):
        
        if i == len(self.word1) and j == len(self.word2):
            return 0
        
        if i == len(self.word1): return len(self.word2) - j
        if j == len(self.word2): return len(self.word1) - i

        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        if self.word1[i] == self.word2[j]:
            self.memo[i][j] = self.__memoizattion(i+1, j+1)
            return self.memo[i][j]
        else:
            self.memo[i][j] = 1 + min(self.__memoizattion(i+1, j),
                                      self.__memoizattion(i+1, j+1),
                                      self.__memoizattion(i, j+1)
                                      )
            return self.memo[i][j]
        
# @lc code=end

