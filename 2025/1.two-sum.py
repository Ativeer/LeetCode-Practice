#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for ind, num in enumerate(nums):
            if target - num in complement:
                return [ind, complement[target-num]]
            complement[num] = ind
        
# @lc code=end

