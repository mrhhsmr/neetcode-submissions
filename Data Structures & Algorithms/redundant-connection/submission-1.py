class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] * (len(edges) + 1)
        for i in range(len(edges) + 1):
            parent[i] = i
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) 
            
            return parent[x]

        def union(i, j):
            rootA = find(i)
            rootB = find(j)
            if rootA == rootB:
                return False 

            parent[rootB] = rootA
            return True
    
        for i, j in edges:
            if not union(i, j):
                return [i, j]

        return []