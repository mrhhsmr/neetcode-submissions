class Solution {
    public boolean validTree(int n, int[][] edges) {
        // 快速判断：树的边数必须等于 n - 1
        // 如果边数不对，要么有环，要么不连通，直接 pass
        if (edges.length != n - 1) return false;

        // 1. 构建邻接表（无向图）
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int i = 0; i < n; i++) adj.put(i, new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        Set<Integer> visited = new HashSet<>();
        
        // 2. 从节点 0 开始 DFS 检查环
        // 传入 -1 作为初始父节点
        if (!hasNoCycle(adj, visited, 0, -1)) {
            return false;
        }

        // 3. 检查是否连通
        return visited.size() == n;
    }

    private boolean hasNoCycle(Map<Integer, List<Integer>> adj, Set<Integer> visited, int curr, int parent) {
        visited.add(curr);

        for (int neighbor : adj.get(curr)) {
            // 关键：如果邻居是我的父节点，忽略它（这不是环，是无向边的回流）
            if (neighbor == parent) continue;
            
            // 如果邻居已经访问过，说明我们通过另一条路绕回来了 -> 有环！
            if (visited.contains(neighbor)) return false;
            
            // 递归检查子路径
            if (!hasNoCycle(adj, visited, neighbor, curr)) return false;
        }

        return true;
    }
}
