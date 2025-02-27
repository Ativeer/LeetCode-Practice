#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (65.70%)
# Likes:    12873
# Dislikes: 178
# Total Accepted:    1.4M
# Total Submissions: 2.2M
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        newgrid = [[math.inf for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.m = len(grid)
        self.n = len(grid[0])

        queue = deque()
        queue.append((0, 0))
        newgrid[0][0] = grid[0][0]

        next_move = [[0, 1], [1, 0]]

        while queue:
            x, y = queue.popleft()
            for i in range(2):
                next_x = x + next_move[i][0]
                next_y = y + next_move[i][1]

                if self.__isValid(next_x, next_y):
                    if newgrid[next_x][next_y] == math.inf:
                        if newgrid[x][y] + grid[next_x][next_y] <= newgrid[-1][-1]:
                            queue.append((next_x, next_y))
                    newgrid[next_x][next_y] = min(newgrid[next_x][next_y], grid[next_x][next_y] + newgrid[x][y])
        return newgrid[-1][-1]

    
    def __isValid(self, x, y):
        if x < 0  or y < 0 or x >= self.m or y >= self.n:
            return False
        return True
        
# @lc code=end

