class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            mp[u].append(v)
            mp[v].append(u)
        
        def dfs(node):
            for nex in mp[node]:
                if not visited[nex]:
                    visited[nex] = True
                    dfs(nex)
        
        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1

        return res