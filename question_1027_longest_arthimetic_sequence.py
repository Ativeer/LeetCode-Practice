class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [{} for _ in range(len(nums))]
        max_len = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[j] - nums[i]
                if diff in dp[j]:
                    dp[i][diff] = 1 + dp[j][diff]
                else:
                    dp[i][diff] = 2
                max_len = max(max_len, dp[i][diff])
        
        return max_len