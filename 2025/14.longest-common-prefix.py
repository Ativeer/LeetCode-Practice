#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (44.70%)
# Likes:    18811
# Dislikes: 4693
# Total Accepted:    4.3M
# Total Submissions: 9.5M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# 
# Example 1:
# 
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
# 
# 
#

# @lc code=start
class Trie:

    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.end = False


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.root = Trie()

        ans = strs[0]

        for i in strs:
            if not i: return ""
            curr_word = ""
            prefix = self.root
            
            for k in range(len(i)):
                if not prefix.children and not prefix.end:
                    newNode = Trie(i[k])
                    prefix.children[i[k]] = newNode
                    prefix = prefix.children[i[k]]
                    curr_word += i[k]
                elif i[k] in prefix.children:
                    prefix = prefix.children[i[k]]
                    curr_word += i[k]
                else:
                    if len(ans) > len(curr_word):
                        ans = curr_word
                        prefix.end = True
                        break
            
            prefix.end = True
            if len(ans) > len(curr_word):
                ans = curr_word

        return ans        
                


        
# @lc code=end

