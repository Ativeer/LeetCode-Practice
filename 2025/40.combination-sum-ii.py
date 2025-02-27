#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (57.07%)
# Likes:    11370
# Dislikes: 336
# Total Accepted:    1.3M
# Total Submissions: 2.3M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note: The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(temp=[], curr_sum=0, pos=0):
            if curr_sum == target:
                ans.append(temp[:])
                return
            
            if curr_sum > target:
                return
            
            for i in range(pos, len(candidates)):
                # break if including current number will cross the target
                if candidates[i] + curr_sum > target: break
                if i != pos and candidates[i] == candidates[i-1]:
                    continue
                backtrack(temp+[candidates[i]], curr_sum+candidates[i], i+1)
        backtrack()
        return ans

# @lc code=end

