#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (55.81%)
# Likes:    13626
# Dislikes: 426
# Total Accepted:    1.1M
# Total Submissions: 2M
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
# 
# 
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# Example 3:
# 
# 
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
# 
# 
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        starting_positions = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    starting_positions.append((i, j))
                    
        time = 0
        def isValid(pos_x, pos_y):
            if pos_x < 0 or pos_x >= len(grid) or pos_y < 0 or pos_y >= len(grid[0]) or grid[pos_x][pos_y] != 1:
                return False
            
            grid[pos_x][pos_y] = 2
            starting_positions.append((pos_x, pos_y))
            return True
        
        def check_neighbor(pos_x, pos_y):
            c1 = isValid(pos_x-1, pos_y)
            c2 = isValid(pos_x, pos_y-1)
            c3 = isValid(pos_x+1, pos_y)
            c4 = isValid(pos_x, pos_y+1)
            return c1 or c2 or c3 or c4

        while starting_positions:
            curr_run = len(starting_positions)
            add_time = False

            for _ in range(curr_run):
                x, y = starting_positions.pop(0)
                if check_neighbor(x, y):
                    add_time = True
            if add_time:
                time += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time




# @lc code=end

