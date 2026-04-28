class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        dfs(nums, target, 0, res, curr);
        return res;
    }

    public void dfs(int[] nums, int target, int index, List<List<Integer>> res, List<Integer> curr){
        if (target < 0){
            return;
        }

        if (target == 0){
            res.add(new ArrayList<>(curr));
            return;
        }

        for(int i = index; i < nums.length; i++){
            curr.add(nums[i]);
            dfs(nums, target - nums[i], i, res, curr);
            curr.remove(curr.size() - 1);
        }
    }
}
