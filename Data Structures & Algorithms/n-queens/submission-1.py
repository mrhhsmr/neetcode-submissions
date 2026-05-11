class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = []
        for _ in range(n):
            board.append(['.'] * n)
        
        def can_place(x , y):
            for col in range(y):
                if board[x][col] == 'Q':
                    return False
 
            i, j = x - 1, y - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1


            i, j = x + 1, y - 1
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i += 1
                j -= 1

            return True
        
        def dfs(j):
            if j == n:
                res.append(["".join(row) for row in board])
                return 
        
            for i in range(n):
                if can_place(i, j):
                    board[i][j] = 'Q'
                    dfs(j + 1)
                    board[i][j] = '.'

        dfs(0)
        return res