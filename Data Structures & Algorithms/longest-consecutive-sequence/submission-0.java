class Solution {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int res = 0;
        for(int i = 0 ; i < nums.length ; i++){
            if(!map.containsKey(nums[i])){
                int left = map.containsKey(nums[i] - 1) ? map.get(nums[i] - 1) : 0;
                int right = map.containsKey(nums[i] + 1) ? map.get(nums[i] + 1) : 0;
                int len = left + right + 1;
                map.put(nums[i], len);
                res = Math.max(res, len);
                map.put(nums[i] - left, len);
                map.put(nums[i] + right, len);
            }
        }

        return res;
    }
}
