class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int res = 0;
        for(int i = 0; i < prices.length; i ++){
            minPrice = Math.min(minPrice, prices[i]);
            res = Math.max(prices[i] - minPrice, res);
        }

        return res;
    }
}
