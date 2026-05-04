class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(index):
            if len(cur) == k:
                res.append(cur.copy())
                return
            
            for i in range(index, n + 1, 1):
                cur.append(i)
                dfs(i + 1)
                cur.pop()
        
        dfs(1)
        return res