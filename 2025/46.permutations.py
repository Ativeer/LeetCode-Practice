#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (79.97%)
# Likes:    19703
# Dislikes: 348
# Total Accepted:    2.5M
# Total Submissions: 3.1M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(temp=[]):
            if len(temp) == len(nums):
                ans.append(temp[:])
                return
            s = set(temp)
            for i in range(len(nums)):
                if nums[i] not in s:
                    backtrack(temp+[nums[i]])
        backtrack()
        return ans



# @lc code=end

