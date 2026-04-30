class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> set = new ArrayList<>();
        int i = 0;
        Arrays.sort(nums);
        dfs(res, set, nums, i);
        return res;
    }

    private void dfs(List<List<Integer>> res, List<Integer> set, int[] nums, int index){
        if(index > nums.length){
            return;
        }

        if(index <= nums.length){
            res.add(new ArrayList<>(set));
        }
       
        for(int i = index; i < nums.length ; i++){
            if(i > index && nums[i] == nums[i - 1]){
                continue;
            }
            set.add(nums[i]);
            dfs(res, set, nums, i + 1);
            set.remove(set.size() - 1);
        }

    }
}
