#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (44.45%)
# Likes:    16496
# Dislikes: 702
# Total Accepted:    2M
# Total Submissions: 4.4M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# Example 1:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# 
# 
# 
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
# 
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def __isValid(x, y, visited, char):
            if (x, y) in visited or x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != char:
                return False
            return True
        
        def dfs(x, y, visited, pos):
            if pos == len(word):
                return True
            next_move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            visited.add((x, y))

            for x_, y_ in next_move:
                next_x = x + x_
                next_y = y + y_
                if __isValid(next_x, next_y, visited, word[pos]):
                    output = dfs(next_x, next_y, visited.copy(), pos+1)
                    if output:
                        return True

            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, set(), 1):
                        return True
        
        return False

# @lc code=end

