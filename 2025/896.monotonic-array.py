#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
# https://leetcode.com/problems/monotonic-array/description/
#
# algorithms
# Easy (61.52%)
# Likes:    3134
# Dislikes: 97
# Total Accepted:    491K
# Total Submissions: 797.6K
# Testcase Example:  '[1,2,2,3]'
#
# An array is monotonic if it is either monotone increasing or monotone
# decreasing.
# 
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# 
# Given an integer array nums, return true if the given array is monotonic, or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,2,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [6,5,4,4]
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,3,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return True
        incr = -1
        counter = 1
        while counter < len(nums):
            if incr == -1:
                
                if nums[counter] > nums[counter-1]:
                    incr = 1
                elif nums[counter] < nums[counter-1]:
                    incr = 0
                counter += 1
                continue

            if incr and nums[counter] < nums[counter-1]:
                return False
            
            if not incr and nums[counter] > nums[counter-1]:
                return False
            counter += 1
        return True
# @lc code=end

