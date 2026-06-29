class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            parent[rootA] = rootB

        for a, b in edges:
            if find(a) == find(b):
                return [a, b]
            else:
                union(a, b)

        return []