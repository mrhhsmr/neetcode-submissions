class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        var set = new HashSet<Integer>();
        int i = 0;
        for (int j = 0 ; j < nums.length ; j++){
            if(j - i > k){
                set.remove(nums[i]);
                i++;
            }

            if (set.contains(nums[j])){
                return true;
            }

            set.add(nums[j]);
        }

        return false;
    }
}