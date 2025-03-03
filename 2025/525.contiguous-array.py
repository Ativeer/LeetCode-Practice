#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (48.92%)
# Likes:    8225
# Dislikes: 421
# Total Accepted:    534.2K
# Total Submissions: 1.1M
# Testcase Example:  '[0,1]'
#
# Given a binary array nums, return the maximum length of a contiguous subarray
# with an equal number of 0 and 1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number
# of 0 and 1.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0:0}
        res = 0
        s = 0
        for ind, val in enumerate(nums, 1):
            if not val:
                s -= 1
            else:
                s += 1
            
            if s in first_seen:
                res = max(res, ind-first_seen[s])
            else:
                first_seen[s] = ind

        return res
            
        
# @lc code=end

