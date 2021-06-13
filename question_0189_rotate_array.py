class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        k %= n
        d = n-k
        
        self.reverse(nums, 0, d-1)
        self.reverse(nums, d, n-1)
        self.reverse(nums, 0, n-1)
        
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1