class Solution {
    public int maxArea(int[] heights) {
        int maxWater = 0;
        int i = 0;
        while ( i < heights.length ){
            int j = heights.length - 1;
            while (i < j){
                maxWater = Math.max(Math.min(heights[i], heights[j]) * (j - i), maxWater);               
                j--;
            }
            i++;
        }

        return maxWater;
    }
}
