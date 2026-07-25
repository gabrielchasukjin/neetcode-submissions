class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        stack = []
        visited = set() 
        
        neigh_nodes = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):

            if (r,c) in visited: 
                return False
            
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] not in word:
                return False
            
            visited.add((r,c))
            stack.append(board[r][c])

            if "".join(stack) == word:
                return True

            if "".join(stack) == word[:len(stack)]: 
                # so far so good

                for r_next, c_next in neigh_nodes:
                    if dfs(r + r_next, c + c_next):
                        return True

            stack.pop()
            visited.remove((r,c))

        
        
        checks = []
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    checks.append(dfs(i,j))
        return any(checks)

                    