from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        result = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum%k in d:
                result += d[curr_sum%k]
            d[curr_sum%k] += 1
        return result