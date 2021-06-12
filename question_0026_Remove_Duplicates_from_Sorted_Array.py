class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count + 1