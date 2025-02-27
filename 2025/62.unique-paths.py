#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (65.31%)
# Likes:    17212
# Dislikes: 463
# Total Accepted:    2.2M
# Total Submissions: 3.4M
# Testcase Example:  '3\n7'
#
# There is a robot on an m x n grid. The robot is initially located at the
# top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
# either down or right at any point in time.
# 
# Given the two integers m and n, return the number of possible unique paths
# that the robot can take to reach the bottom-right corner.
# 
# The test cases are generated so that the answer will be less than or equal to
# 2 * 10^9.
# 
# 
# Example 1:
# 
# 
# Input: m = 3, n = 7
# Output: 28
# 
# 
# Example 2:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach
# the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 100
# 
# 
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from collections import deque
        self.m = m
        self.n = n

        queue = deque()
        queue.append((0, 0))

        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][0] = 1
        next_move = [[0, 1], [1, 0]]

        while queue:
            x, y = queue.popleft()
            for i in range(2):
                next_x = x + next_move[i][0]
                next_y = y + next_move[i][1]
                if self.__isValid(next_x, next_y):
                    if grid[next_x][next_y] == 0:
                        queue.append((next_x, next_y))
                    grid[next_x][next_y] += grid[x][y]

        return grid[-1][-1]


    def __isValid(self, x, y):
        if x >= self.m or y >= self.n:
            return False
        return True        


# @lc code=end

