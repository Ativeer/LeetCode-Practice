class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        def dfs(row, column, visited):
            if visited[row][column] != 0:
                return visited[row][column]
            
            for d in directions:
                pos1 = row + d[0]
                pos2 = column + d[1]
                if pos1 >= 0 and pos1 < len(matrix) and pos2 >= 0 and pos2 < len(matrix[0]) and matrix[pos1][pos2] > matrix[row][column]:
                    visited[row][column] = max(visited[row][column], dfs(pos1, pos2, visited))
            visited[row][column] += 1
            return visited[row][column]

        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j, visited))
        return ans