class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # self.length = len(nums)
        # self.nums.sort()
        def helper(a, temp=[]):
            ans.append(temp)
            for i in range(len(a)):
                if i > 0 and a[i] == a[i-1]:
                    continue
                helper(a[i+1:], temp+[a[i]])
        
        helper(sorted(nums))

        return ans

## Approach 2
# Slower but naive
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.length = len(nums)
        self.nums = nums
        self.nums.sort()
        def helper(temp=[], counter=0):
            ans.append(temp)
            
            for i in range(counter, self.length):
                temp.append(self.nums[i])
                helper(temp.copy(), i+1)
                temp.pop()
        
        helper()
        final_ans = []
        for i in ans:
            if i in final_ans:
                continue
            final_ans.append(i)
        return final_ans