#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#
# https://leetcode.com/problems/count-sub-islands/description/
#
# algorithms
# Medium (72.83%)
# Likes:    2551
# Dislikes: 89
# Total Accepted:    201.3K
# Total Submissions: 276.4K
# Testcase Example:  '[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]\n' +
  # '[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]'
#
# You are given two m x n binary matrices grid1 and grid2 containing only 0's
# (representing water) and 1's (representing land). An island is a group of 1's
# connected 4-directionally (horizontal or vertical). Any cells outside of the
# grid are considered water cells.
# 
# An island in grid2 is considered a sub-island if there is an island in grid1
# that contains all the cells that make up this island in grid2.
# 
# Return the number of islands in grid2 that are considered sub-islands.
# 
# 
# Example 1:
# 
# 
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are three sub-islands.
# 
# 
# Example 2:
# 
# 
# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2 
# Explanation: In the picture above, the grid on the left is grid1 and the grid
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are two sub-islands.
# 
# 
# 
# Constraints:
# 
# 
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] and grid2[i][j] are either 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= len(grid1) or y < 0 or y >= len(grid1[0]) or grid2[x][y] == 0:
                return
            
            grid2[x][y] = 0

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(i, j)

        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    count += 1
        return count        

# @lc code=end

