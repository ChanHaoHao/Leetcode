class Solution {
    public int maxProfit(int[] prices) {
        int curMin=prices[0], ans=0;
        for (int i:prices) {
            curMin=Math.min(curMin, i);
            ans=Math.max(ans, i-curMin);
        }

        return ans;
    }
}