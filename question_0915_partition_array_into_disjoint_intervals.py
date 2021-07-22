class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = [nums[-1] for _ in range(len(nums))]
        for i in range(len(nums)-2, 0, -1):
            min_so_far[i] = min(min_so_far[i+1], nums[i])
        
        for i in range(1, len(nums)):
            max_so_far = max(max_so_far, nums[i-1])
            if max_so_far <= min_so_far[i]:
                return i