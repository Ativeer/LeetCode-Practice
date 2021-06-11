class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        def helper(nums, temp=[], counter=0):
            ans.append(temp)
            
            
            if counter == length:
                return
            
            for i in range(counter, length):
                
                temp.append(nums[i])
                helper(nums, temp.copy(), i+1)
                temp.pop()
        
        helper(nums)
        return ans