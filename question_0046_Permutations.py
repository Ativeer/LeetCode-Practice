class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        ans = []
        
        def helper(idx=0):
            if idx == length:
                ans.append(nums[:])
                return
            
            for i in range(idx, length):
                nums[idx], nums[i] = nums[i], nums[idx]
                helper(idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]
        helper()
        return ans