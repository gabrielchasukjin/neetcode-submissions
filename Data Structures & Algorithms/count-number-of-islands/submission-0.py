class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set() 

        neighbors = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r,c):
            if (r,c) in visited:
                return False
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0":
                return False
            visited.add((r,c))

            for next_r, next_c in neighbors: 
                dfs(r+next_r, c+next_c)

        
        islands = 0 
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    # dfs finishes means an island was completed 
                    islands += 1 
        return islands 
        