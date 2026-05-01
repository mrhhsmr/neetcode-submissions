class Solution {
    public int trap(int[] height) {
        if(height == null || height.length == 0){
            return 0;
        }

        int res = 0;
        int n = height.length;
        for(int i = 0 ; i < height.length ; i++){
            int leftMax = height[i];
            int rightMax = height[i];
            for(int j = 0; j < i ; j++){
                leftMax = Math.max(leftMax, height[j]);
            }

            for(int j = i + 1; j < height.length ; j++){
                rightMax = Math.max(rightMax, height[j]);
            }

            res += Math.min(leftMax, rightMax) -  height[i];

        }

        return res;
    }
}
