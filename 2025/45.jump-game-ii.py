#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (41.05%)
# Likes:    15273
# Dislikes: 631
# Total Accepted:    1.6M
# Total Submissions: 3.9M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0].
# 
# Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at nums[i], you can jump to any nums[i +
# j] where:
# 
# 
# 0 <= j <= nums[i] and
# i + j < n
# 
# 
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,3,0,1,4]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].
# 
# 
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        dp = [math.inf for _ in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)):
            jump_cap = i + nums[i]
            if jump_cap >= len(nums) - 1:
                return dp[i] + 1
            else:
                for j in range(i+1, jump_cap+1):
                    dp[j] = min(dp[j], dp[i]+1)
        return dp[-1]
            


# @lc code=end

