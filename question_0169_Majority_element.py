class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] != me:
                if count == 0:
                    count = 1
                    me = nums[i]
                else:
                    count -= 1
            else:
                count += 1
        return me