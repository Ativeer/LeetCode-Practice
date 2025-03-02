#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (73.05%)
# Likes:    9587
# Dislikes: 249
# Total Accepted:    2.1M
# Total Submissions: 2.9M
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# 
# 
# Example 2:
# 
# 
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
# 
# 
# 
# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [i**2 for i in nums]
        ans = []
        neg_ind = -1
        pos_ind = 0
        while pos_ind < len(nums) and nums[pos_ind] < 0:
            pos_ind += 1
            neg_ind += 1

        
        while neg_ind >= 0 and pos_ind < len(nums):
            pos_sq = nums[pos_ind] ** 2
            neg_sq = nums[neg_ind] ** 2
            if neg_sq < pos_sq:
                ans.append(neg_sq)
                neg_ind -= 1
            else:
                ans.append(pos_sq)
                pos_ind += 1
        
        while neg_ind >= 0:
            ans.append(nums[neg_ind]**2)
            neg_ind -= 1
        
        while pos_ind < len(nums):
            ans.append(nums[pos_ind]**2)
            pos_ind += 1
        return ans
        

        
# @lc code=end

