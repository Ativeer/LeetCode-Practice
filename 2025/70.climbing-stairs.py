#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Recurssion
        '''
        # if n < 0: return 0
        # if n == 0: return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        '''
        memoization
        '''
        # memo = [-1 for _ in range(n+1)]
        # def run_memo(lvl):
        #     nonlocal memo
        #     if lvl < 0: return 0
        #     if lvl == 0: return 1
        #     if memo[lvl] != -1:
        #         return memo[lvl]
        #     memo[lvl] = run_memo(lvl-1) + run_memo(lvl-2)
        #     return memo[lvl]
        # run_memo(n)
        # return memo[-1]

        '''
        dp
        '''
        if n == 1: return 1
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

# @lc code=end

