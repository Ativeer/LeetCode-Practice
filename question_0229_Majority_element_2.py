class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter1 = 0
        counter2 = 0
        n1 = None
        n2 = None
        if not nums:
            return []
        
        for n in nums:
            if n == n1:
                counter1 += 1
            elif n == n2:
                counter2 += 1
            elif counter1 == 0:
                counter1 = 1
                n1 = n
            elif counter2 == 0:
                counter2 = 1
                n2 = n
            else:
                counter1 -= 1
                counter2 -= 1
        ans = []
        
        for c in [n1, n2]:
            if nums.count(c) > len(nums)//3:
                ans.append(c)
        return ans