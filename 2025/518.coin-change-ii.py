#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#
# https://leetcode.com/problems/coin-change-ii/description/
#
# algorithms
# Medium (63.33%)
# Likes:    9638
# Dislikes: 194
# Total Accepted:    754.1K
# Total Submissions: 1.2M
# Testcase Example:  '5\n[1,2,5]'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# 
# Return the number of combinations that make up that amount. If that amount of
# money cannot be made up by any combination of the coins, return 0.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# The answer is guaranteed to fit into a signed 32-bit integer.
# 
# 
# Example 1:
# 
# 
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# Example 2:
# 
# 
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# 
# 
# Example 3:
# 
# 
# Input: amount = 10, coins = [10]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000
# 
# 
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # backtracking
        # total_count = 0

        # def backtrack(curr_index, curr_sum):
        #     if curr_sum == amount:
        #         nonlocal total_count
        #         total_count += 1
        #         return
        #     if curr_sum > amount or curr_index >= len(coins):
        #         return

        #     # include coin
        #     backtrack(curr_index, curr_sum+coins[curr_index])
        #     backtrack(curr_index+1, curr_sum)
        # backtrack(0, 0)
        # return total_count
        

# @lc code=end
