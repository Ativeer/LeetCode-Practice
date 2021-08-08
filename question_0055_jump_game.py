# greedy
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0


# DP

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[0] = True
        last_true = 0
        for i in range(len(nums)):
            if not dp[i]:
                return False
            if last_true-i < nums[i]:
                remaining_values = nums[i] + i - last_true
                for j in range(last_true, min(nums[i] + i + 1, len(nums))):
                    dp[j] = True
                    last_true = j
                if last_true == len(nums):
                    return True

                
                
        return dp[-1]