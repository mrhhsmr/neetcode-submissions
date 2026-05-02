class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    def dfs(board, i, j, word, k):
                        if k == len(word):
                            return True

                        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                            return False

                        if board[i][j] != word[k] or board[i][j] == '#':
                            return False
                        
                        board[i][j] = '#'
                        res = dfs(board, i + 1, j, word, k + 1) or \
                        dfs(board, i - 1, j, word, k + 1) or \
                        dfs(board, i, j + 1, word, k + 1) or \
                        dfs(board, i, j - 1, word, k + 1)
                        board[i][j] = word[k]
                        return res;
                    
                    res = dfs(board, i, j, word, 0)
                    if res:
                        return True

        return False
        