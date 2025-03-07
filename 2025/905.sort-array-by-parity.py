#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (76.27%)
# Likes:    5482
# Dislikes: 153
# Total Accepted:    881.2K
# Total Submissions: 1.2M
# Testcase Example:  '[3,1,2,4]'
#
# Given an integer array nums, move all the even integers at the beginning of
# the array followed by all the odd integers.
# 
# Return any array that satisfies this condition.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be
# accepted.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
# 
# 
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pivotIdx = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[pivotIdx], nums[i] = nums[i], nums[pivotIdx]
                pivotIdx += 1
        return nums

# @lc code=end

