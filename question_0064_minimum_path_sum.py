class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        
        def dfs(posx, posy):
            if posx >= n or posy >= m:
                return math.inf
            if posx == n-1 and posy == m-1:
                return grid[posx][posy]
            
            if visited[posx][posy] == 0:
                visited[posx][posy] = grid[posx][posy] + min(dfs(posx+1, posy), dfs(posx, posy+1))
            
            return visited[posx][posy]
        
        return dfs(0, 0)