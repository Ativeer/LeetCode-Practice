#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (54.78%)
# Likes:    9153
# Dislikes: 140
# Total Accepted:    606.1K
# Total Submissions: 1.1M
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an m x n integers matrix, return the length of the longest increasing
# path in matrix.
# 
# From each cell, you can either move in four directions: left, right, up, or
# down. You may not move diagonally or move outside the boundary (i.e.,
# wrap-around is not allowed).
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        Memoized DFS
        '''
        #     if not matrix or not matrix[0]:
        #         return 0
                    
        #     self.visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        #     ans = 0
        #     for a in range(len(matrix)):
        #         for b in range(len(matrix[0])):
        #             if self.visited[a][b] == 0:
        #                 ans = max(ans, self.__dfs(a, b, matrix))
        #     return ans

        
        # def __dfs(self, i: int, j: int, matrix: List[List[int]]) -> int:
        #     _max = 0
        #     directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        #     if not self.visited[i][j]:
        #         curr_val = matrix[i][j]
        #         for x_, y_ in directions:
        #             new_x = i + x_
        #             new_y = j + y_
        #             if Solution.__isValid(new_x, new_y, matrix, curr_val):
        #                 _max = max(_max, self.__dfs(new_x, new_y, matrix))
        #         self.visited[i][j] = _max + 1
        #     return self.visited[i][j]

        # @staticmethod
        # def __isValid(x: int, y: int, grid: List[List[int]], prev_value: int) -> bool:
        #     if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] <= prev_value:
        #         return False
        #     return True
        '''
        DAG/Topological Sorting
        '''
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.indegree = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] < matrix[i][j]:
                        self.indegree[i][j] += 1
        

        q = deque()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not self.indegree[i][j]:
                    q.append((i, j))

        max_path = 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in directions:
                    
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] > matrix[i][j]:
                        self.indegree[ni][nj] -= 1
                        if not self.indegree[ni][nj]:
                            q.append((ni, nj))
            max_path += 1
        return max_path


        

        
# @lc code=end

