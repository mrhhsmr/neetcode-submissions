class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    if board[i][j] == 'O':
                        def dfs(i, j):
                            if i < 0 or i == row or j < 0 or j == col or board[i][j] != 'O':
                                return
                            
                            board[i][j] = '1'
                            dfs(i + 1, j)
                            dfs(i - 1, j)
                            dfs(i, j + 1)
                            dfs(i, j -1)
                    
                        dfs(i, j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == '1':
                    board[i][j] = 'O'

 