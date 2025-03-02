#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
#
# algorithms
# Easy (83.64%)
# Likes:    2838
# Dislikes: 60
# Total Accepted:    413.8K
# Total Submissions: 494.5K
# Testcase Example:  '"thequickbrownfoxjumpsoverthelazydog"'
#
# A pangram is a sentence where every letter of the English alphabet appears at
# least once.
# 
# Given a string sentence containing only lowercase English letters, return
# true if sentence is a pangram, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English
# alphabet.
# 
# 
# Example 2:
# 
# 
# Input: sentence = "leetcode"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # bucket = [0]*26

        # for i in sentence:
        #     idx = ord(i) - ord('a')
        #     bucket[idx] = 1
        
        # for i in bucket:
        #     if not i:
        #         return False
        # return True

        # visited = set()
        # for i in sentence:
        #     visited.add(i)
        # return len(visited) == 26

        visited = set("abcdefghijklmnopqrstuvwwxyz")
        for i in sentence:
            if i in visited:
                visited.remove(i)
        return visited == set()

# @lc code=end

