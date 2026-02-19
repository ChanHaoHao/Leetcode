int maxProfit(int* prices, int pricesSize) {
    int ans = 0, buy = prices[0];
    for (int i=1; i<pricesSize; ++i) {
        if (prices[i] - buy > ans) {
            ans = prices[i] - buy;
        }

        if (prices[i] < buy) {
            buy = prices[i];
        }
    }

    return ans;
}