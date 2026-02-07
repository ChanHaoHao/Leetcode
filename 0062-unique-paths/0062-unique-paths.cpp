class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 0);
        dp[n - 1] = 1;

        for (m; m>0; --m) {
            for (int i=n-2; i>=0; --i) {
                dp[i] += dp[i+1];
            }
        }

        return dp[0];
    }
};