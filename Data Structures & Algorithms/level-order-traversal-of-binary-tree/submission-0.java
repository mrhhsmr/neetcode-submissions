/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if(root == null){
            return res;
        }

        var q = new LinkedList<TreeNode>();
        q.offer(root);
        while(!q.isEmpty()){
            int size = q.size();
            var list = new ArrayList<Integer>();
            for ( int i = 0; i < size ; i++){
                var n = q.poll();
                list.add(n.val);
                if(n.left != null){
                    q.offer(n.left);
                }

                if(n.right != null){
                    q.offer(n.right);
                }
            }
            res.add(list);
        }

        return res;
    }
}
