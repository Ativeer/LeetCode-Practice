class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j, islandID):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return 0

            grid[i][j] = islandID
            l = dfs(grid,i,j-1,islandID)
            r = dfs(grid,i,j+1,islandID)
            t = dfs(grid,i-1,j,islandID)
            b = dfs(grid,i+1,j,islandID)
            return l + r + t + b + 1
                
        
        directions=[[1,0], [-1,0], [0,1], [0,-1]]

        maxx = 0
        islandID = 2
        m = len(grid)
        
        mapp = {}
        for i in range(0, m):
            for j in range (0, m):
                
                if grid[i][j] == 1:
                    size = dfs(grid, i, j, islandID)
                    maxx = max(maxx, size)
                    mapp[islandID] = size
                    islandID += 1

        for i in range(0, m):
            for j in range(0, m):
                if grid[i][j] == 0:
                    sett = set()
                    for direction in directions:
                        x = direction[0] + i
                        y = direction[1] + j
                        if x > -1 and y > -1 and x < m and y < m and grid[x][y] != 0:
                            sett.add(grid[x][y])

                    summ = 1
                    
                    for num in sett:
                        value = mapp[num]
                        summ += value
                    maxx = max(maxx,summ)
                    
        return maxx