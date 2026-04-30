class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();

        dfs(nums, res, curr);
        return res;
    }

    private void dfs(int[] nums, List<List<Integer>> res, List<Integer> curr){
        if(curr.size() == nums.length){
            res.add(new ArrayList<>(curr));
            return;
        }

        for(int i = 0; i < nums.length ; i++){
            if(!curr.contains(nums[i])){
                curr.add(nums[i]);
                dfs(nums, res, curr);
                curr.remove(curr.size() - 1);
            }
        }
    }
}
