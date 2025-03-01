#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (47.82%)
# Likes:    6584
# Dislikes: 3194
# Total Accepted:    1.2M
# Total Submissions: 2.6M
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
# - j) <= k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: return False
        visited_set = set()
        start = 0
        end = 1
        visited_set.add(nums[0])


        while end < len(nums):
            curr_ = nums[end]
            if curr_ in visited_set:
                return True
            if (end - start) == k:
                visited_set.remove(nums[start])
                start += 1
            visited_set.add(curr_)
            end += 1
        return False



# @lc code=end

