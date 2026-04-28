class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        dfs(res, 0, nums, curr);
        return res;
    }

    public void dfs(List<List<Integer>> res, int index, int[] nums, List<Integer> curr){
        res.add(new ArrayList<>(curr));
        if (index == nums.length){
            return;
        }

        for(int i = index ; i < nums.length ; i++){
            curr.add(nums[i]);
            dfs(res, i + 1, nums, curr);
            curr.remove(curr.size() - 1);
        }
    }
}
