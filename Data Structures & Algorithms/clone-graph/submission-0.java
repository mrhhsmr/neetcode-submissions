/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        var map = new HashMap<Node, Node>();
        cloneGraph(map, node);
        for(var mapset : map.entrySet()){
            var clonedNode = mapset.getValue();
            var oNode = mapset.getKey();
            for(var next : oNode.neighbors){
                clonedNode.neighbors.add(map.get(next));
            }
        }
        return map.get(node);
    }

    public void cloneGraph(Map<Node, Node> map, Node node){
        if (node == null || map.containsKey(node)){
            return;
        }

        var clonedNode = new Node(node.val);
        map.put(node, clonedNode);
        for(var next : node.neighbors){
            cloneGraph(map, next);
        }  
    }
}