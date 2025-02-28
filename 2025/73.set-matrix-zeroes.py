#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (58.68%)
# Likes:    15339
# Dislikes: 780
# Total Accepted:    1.8M
# Total Submissions: 3.1M
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire row
# and column to 0's.
# 
# You must do it in place.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
# 
# 
# 
# Follow up:
# 
# 
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        first_row = True if 0 in matrix[0] else False
        first_col = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col = True
                break


        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    # convert first row as 0
                    # convert first col as 0 too
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0
        
        if first_row:
            matrix[0] = [0 for _ in range(len(matrix[0]))]
        
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        

# @lc code=end

