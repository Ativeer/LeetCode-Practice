#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (58.75%)
# Likes:    10169
# Dislikes: 359
# Total Accepted:    1.1M
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        visited = set()

        def backtrack(temp=[], ptr=0):
            ans.append(temp[:])
            visited.add(tuple(temp))
            for i in range(ptr, len(nums)):
                temp.append(nums[i])
                if tuple(temp) not in visited:
                    backtrack(temp, i+1)
                temp.pop()

                
        backtrack()
        return ans

# @lc code=end

