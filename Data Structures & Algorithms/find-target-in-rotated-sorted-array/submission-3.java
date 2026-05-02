class Solution {
    public int search(int[] nums, int target) {
        int start = 0, end = nums.length - 1;
        while(start <= end){
            int mid = start + (end - start ) / 2;
            if(nums[mid] == target){
                return mid;
            }
            else{
                if(nums[start] <= nums[mid]){
                    //左边乱序，右边
                    if(target > nums[mid] || target < nums[start]){
                        start = mid + 1;
                    }
                    else{
                        end = mid - 1;
                    }
                }
                else{
                    //右边乱序，所以在左边
                    if(target < nums[mid] || target > nums[end]){
                        end = mid - 1;
                    }
                    else{
                        start = mid + 1;
                    }
                }
            }
        }

        return -1;
    }
}
