class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set() 

        def dfs(r,c):

            if (r,c) in visited : 
                return 0
            
            if (r >= row or r < 0 or c >= col or c < 0)or grid[r][c] == 0 : 
                return 1 
            
            visited.add((r,c))

            return dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        for i in range(row):
            for j in range(col): 

                if grid[i][j] == 1:
                    return dfs(i, j)

        return 0  

      