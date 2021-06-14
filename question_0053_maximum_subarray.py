class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = nums[0]
        prev = nums[0]
        for i in range(1, len(nums)):
            temp = prev + nums[i]
            prev = max(temp, nums[i])
            m = max(m, prev)
        return m