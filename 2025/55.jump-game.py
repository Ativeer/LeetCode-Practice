#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (39.04%)
# Likes:    20219
# Dislikes: 1358
# Total Accepted:    2.4M
# Total Submissions: 6.2M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.
# 
# Return true if you can reach the last index, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Finding max jump from start
        '''
        # farthest = 0
        # for i in range(len(nums)):
        #     if i > farthest:
        #         return False
        #     farthest = max(farthest, i + nums[i])
        #     if farthest >= len(nums)-1:
        #         return True
        '''
        Finding max jump from end
        '''
        final_pos = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= final_pos:
                final_pos = i
        return final_pos == 0



# @lc code=end

