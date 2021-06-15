class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s = sum(nums)
        m = nums[0]
        prev = nums[0]
        
        for i in range(1, len(nums)):
            curr = prev + nums[i]
            prev = max(nums[i], curr)
            m = max(m, prev)
        
        mi = nums[0]
        prev = nums[0]
        
        for i in range(1, len(nums)):
            curr = prev + nums[i]
            prev = min(nums[i], curr)
            mi = min(mi, prev)
        
        # Edge Case
        if s == mi:
            return m
        return max(m, s-mi)