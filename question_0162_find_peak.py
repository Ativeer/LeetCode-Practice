class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        if len(nums) == 1:
            return 0
        end = len(nums) - 1
        while end >= start:
            mid = (start+end)//2
            if mid == 0 and nums[mid] > nums[mid+1]:
                return 0
            if mid == len(nums)-1 and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] > nums[mid+1]:
                end = mid - 1
            else:
                start = mid + 1
            