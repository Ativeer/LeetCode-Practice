class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if not nums:
            return []
        if nums[0] > 0 or nums[-1] < 0:
            return []
        output = []
        for i in range(len(nums)-2):
            d = {}
            for j in range(i+1, len(nums)):
                if (nums[j]) in d and [nums[i], nums[j], d[nums[j]]] not in output:
                    output.append([nums[i], nums[j], d[nums[j]]])
                else:
                    d[-nums[i]-nums[j]] = nums[j]
        return output